# Sample testing scopes

Samples in the house style, written for a made-up helpdesk app called Relay (Inbox, Customers, Automations, Campaigns, Reports, Settings). Match their length, tone and shape. Copy the habits, not the content.

## Contents

1. PRD sections in a flight doc (delta only)
2. Bug fix tickets
3. Tech improvements with a wide blast radius
4. PR body style

---

## 1. PRD sections in a flight doc (delta only)

The flight doc opens with one line saying what it covers:

```
## Flight

Only items that aren't covered by the PRD, or where the code behaves differently from what you'd expect.
```

A section with real gotchas found in the code:

```
>>> ### Section 1: Attachments in SMS replies

* Nothing in our app blocks file types or sizes for SMS. Files go to the SMS provider, and it rejects bad ones. Check the failed reply shows the provider's reason for:
  * a file type that isn't on the list (DOCX, HEIC, MOV)
  * a file between 5 MB and 10 MB. Our upload allows 10 MB, but the provider is said to cap at 5 MB (not confirmed in backend code)
* Image with a caption: check the caption reaches the phone
* Inbound: if a customer sends several photos in one message, only the first one is kept
* Others as per PRD.

>>>
```

Changed behaviour and a PM question:

```
>>> ### Section 4: Email channel setup

* New: the leave warning shows as soon as anything is typed. Before, it only showed on step 2
* Changed: the "Send test email" link on the success page used to open a blank tab. Check it now opens the composer for every email provider: Gmail, Outlook and SMTP
* Others as per PRD.

>>>

>>> ### Section 6: Inbox

* Customer matching: an SMS from a number that already belongs to an email customer creates a **new** customer. It doesn't join the existing one. Confirm with PM that this is acceptable
* Failed reply tooltip: provider error 4031 shows "Reply window has closed", which is misleading because SMS has no reply window. Raise it with BE if it appears
* Others as per PRD.

>>>
```

Nothing to add:

```
>>> ### Section 2: Channel catalog

* As per PRD.

>>>
```

A PRD gap turned into a question, plus regression on existing data:

```
>>> ### Section 3: New trigger in Automations

* Condition on `first_message_channel`: pick SMS, save, reload the automation → still selected. Try "is", "is not", and SMS combined with other values.
* Existing automations using other values still open, save and run as before.
* Automation is waiting for the customer's answer (Ask a question step) and the customer only sends a sticker → note what happens: taken as the answer, treated as invalid, or ignored. The PRD doesn't say, so check with PM.
* Others as per PRD.

>>>
```

Setup notes that apply to every section go in a short block at the top:

```
>>> **Before you start**

* Run each scenario on all 3 providers: Twilio, Vonage, Plivo. Each one sends delivery receipts slightly differently.
* Check each scenario twice: live as it arrives, and again after a page refresh. Both should look the same.

>>>
```

Regression from shared code goes in its own section after the PRD sections:

```
### Outside the PRD: regression from shared code changes

* Connect, rename and delete for every channel now go through shared code. Smoke-test a few non-SMS channels: Email, Live chat and WhatsApp
```

---

## 2. Bug fix tickets

Small fix, with sub-groups in bold and nested results:

```
>>> APP-412 Ticket creator tooltip missing on hover

**Core fix: custom views**

* Hover a view someone else created, in **All** and **Shared with me**:
  * "Created by <name>" appears after about 500ms
  * It sits below the item
* Hover your own view, in **All** and **Created by me** → no tooltip

**Where the tooltip must stay hidden**

* Default views (All, Mine, Unassigned)
* Team views and Spam

**Interactions on the item (the tooltip now adds its own mouse handlers)**

* Click a view → it opens its ticket list, and the tooltip closes
* ⋯ menu on your own view:
  * Edit opens the filter drawer
  * Delete opens the confirm dialog
  * The tooltip doesn't block the menu

>>>
```

Fix that removes a request, checked from several entry points:

```
>>> APP-377 Stop loading reply settings before a workspace is picked

* Sign up a new account: no `/reply-settings` call in the Network tab on the create workspace page
* Log in to an existing workspace: reply settings still load
* Close a ticket where a closing note is required → closing note dialog still shows
* Close a ticket from the command palette → still works, and asks for the note when required

>>>
```

Realtime behaviour with a regression line:

```
>>> APP-455 Show edited messages from live chat

* Customer edits their latest message with the ticket open:
  * Bubble shows the new text + "Edited"
  * List preview shows `<text> (edited)` without reloading
* Customer edits while you're in another ticket → list preview updates; open it → new text, no old text first
* Customer edits an older message → bubble updates, preview stays on the latest message
* Edit never bumps the unread count, plays a sound or moves the ticket to the top
* Regression: link previews, deleted messages and the translate toggle work as before

>>>
```

Setup, numbered cases and a known limit:

```
>>> APP-502 Saved replies lose their attachments after a failed upload

*Setup*

* A saved reply with 2 attachments
* DevTools → Network → Slow 3G

*Main cases*

1. Settings → Saved replies → edit → add a third file, then go offline mid-upload
   * The failed file shows an error
   * The other 2 attachments stay
2. Go back online → Save → reopen the saved reply → only the 2 good files are there
3. Insert the saved reply in a ticket with `/` → both files attach to the composer

*Known, not a bug*

* A failed upload can't be retried in place. Remove it and add it again (same as before)

>>>
```

A one-liner is fine when that's all there is:

```
>>> APP-389 Wrong button label on one-time code templates

* Create a one-time code template, open it in the template list before approval → preview shows "Copy code"

>>>
```

---

## 3. Tech improvements with a wide blast radius

Prioritise when the change touches many screens:

```
>>> APP-521 Upgrade the file upload library to v5

**P0: Inbox**

1. **Reply composer:** attach an image, a PDF and a video, then send
   * Progress bar shows during upload and hides when done
   * Thumbnails show for images
2. **Cancel or remove:** remove a file before sending, and cancel a large one mid-upload → nothing gets sent
3. **Switching tickets:** start an upload, switch ticket and back → files stay with the right ticket

**P1: Other upload flows**

* **Customers:** import a CSV
* **Automations:** Send message step attachment
* **Campaigns:** builder file block
* **Settings:** profile picture crop; SSO metadata file

>>>
```

A change in one shared place, with a timing gotcha up front:

```
>>> APP-466 Time zones ignore daylight saving time

**What changed:** time zone offsets now follow daylight saving time. It's one shared helper, so every time zone dropdown and label in the app is affected.

> Test before **Oct 25**. Spain leaves daylight saving time that day. After that, old and new both show Madrid as GMT+01:00, so the test proves nothing. If you test later, use **Australia/Sydney (GMT+11:00)**.

**Steps** (check each module)

1. **Automations:** add a **Wait until** step → Time zone **Europe/Madrid** → save. Check the dropdown and the step label
2. **Settings → Workspace → Time zone:** set **Europe/Madrid**. Set it back when you're done
3. **Campaigns → Schedule:** pick **Europe/Madrid** and schedule. Check the time zone in the details drawer

**You should see**

* **Europe/Madrid** shows **(GMT+02:00)** everywhere, not (GMT+01:00)
* Each dropdown lists zones from most negative offset to most positive. Search still works
* Automations and campaigns saved before this change still show their time zone. If one shows "UTC", note which zone it had and tell me

>>>
```

---

## 4. PR body style

"Validate that" bullets, with (new) for new behaviour:

```
## QA testing scope

- Validate that on Create workspace (a new sign-up), the Sign in link shows the "Leave setup?" dialog, even on an untouched form
- Validate that Cancel keeps the form filled, and Leave goes straight to login with no browser prompt
- Validate that refreshing or closing the tab mid-setup shows the browser's leave prompt
- Validate that browser Back away from setup now shows the dialog (new)
- Validate that finishing all 3 steps lands in the workspace with no dialog or prompt
```

Numbered steps when the setup is fiddly, with a regression line for shared components:

```
## QA testing scope

1. Workspace needs a help article that failed to import (red error icon)
2. Settings → Knowledge base → Articles → hover the red icon
   * The failure reason shows in a tooltip
3. Regression: the failed row still can't be selected, and the processing tooltip still works on the list and on the article cards, which share this component
```

Risk level and a smoke list for refactors:

```
## QA testing scope

Medium risk. Smoke test: connect a new channel (it shows once in the list), and reconnect an existing one (no duplicate).
```

Say plainly what can't be tested by hand:

```
Not manually testable, covered by unit tests only:
- **Calendar re-auth:** needs the calendar API to return 401, which QA can't force on staging
- **Legacy SMS provider:** deprecated and no longer in the channel catalog
```
