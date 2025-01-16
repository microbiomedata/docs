# Submitting in the field: NMDC Field Notes

# Beta Testing

| ⚠️ | The NMDC Field Notes app is beta software and may contain bugs. Some bugs may result in data loss. Do not use it as your sole source of recordkeeping. |
| ----: | :---- |

Thank you for your interest in beta testing the NMDC Field Notes app.

## How to get the app

### Apple users (e.g. iPhone, iPad)

For Apple users, beta versions of the app are distributed via Apple’s [TestFlight](https://testflight.apple.com/) app. First, email [support@microbiomedata.org](mailto:support@microbiomedata.org) with a list of names and email addresses of testers. We will generate invitations to access the app via TestFlight. Testers will receive an email with instructions on how to install the TestFlight app (if necessary) and accept the invitation to use NMDC Field Notes through TestFlight. Testers should follow the email’s instructions on the device they plan to test with.

| ℹ️ | We recommend enabling automatic updates to have notifications sent for the latest beta builds. In TestFlight, select the NMDC Field Notes app. Under “App Information”, confirm that Automatic Updates is turned on. When new builds are available, a notification will be sent and you will be prompted to update to the latest version.  |
| ----: | :---- |

### Android users

For Android users, beta versions of the app are distributed via [APK](https://en.wikipedia.org/wiki/Apk_\(file_format\)) files attached to GitHub Releases.

1. On the device you’d like to test with, open [https://github.com/microbiomedata/nmdc-field-notes/releases/latest](https://github.com/microbiomedata/nmdc-field-notes/releases/latest).   
2. From the Assets section at the bottom of the page, download the `org.microbiomedata.fieldnotes-***.apk` file (the asterisks represent version and build information that will change with each release).  
   1. If prompted with a “File might be harmful” popup, tap “Download anyway”.  
3. Open the downloaded APK file to install it.   
   1. If prompted with an “Open with” menu, select “Package installer” (or equivalent).  
   2. If prompted with a message about not being able to install unknown apps from this source, following the prompt to open Settings and enable the “Allow from this source” setting. Once the app is installed, you may disable this setting again for security reasons.  
   3. If prompted with an “App scan recommended” popup, tap the “Scan app” button. Once the scan completes tap the “Install” button.

There is no automatic update process for beta versions on Android devices. Please check the GitHub Releases page regularly to see if newer versions are available. Alternatively you can be notified of new GitHub Releases by visiting [https://github.com/microbiomedata/nmdc-field-notes](https://github.com/microbiomedata/nmdc-field-notes), selecting Watch \> Custom, and checking the Releases checkbox. You must be signed in to GitHub to enable notifications. Note that there may be a delay of up to 20 minutes between when the GitHub Release is created and when the APK file is added to it.

| ℹ️ | Once the app is out of beta testing, it will be installable and receive updates via the Google Play Store. |
| ----: | :---- |

## Known bugs and limitations

Please note that this app is currently in the testing phase, and is not meant to serve as the only resource for collecting sample information. We highly recommend you _also_ record sample information _without_ the NMDC Field Notes app to ensure a stable backup.  

### Offline support

The NMDC Field Notes app is designed to work with or without network access. However, there are a few important limitations to be aware of when using it without network access. Please review these carefully if you intend to work in an area without network access.

* Most features of the app require signing in via [ORCID](https://orcid.org/) in order to get your NMDC user profile and any existing studies associated with your account. That information will be stored for offline use, but the **initial sign-in must be done while you have network access**.  
* Creating and deleting studies cannot be done while offline. *Updating* studies (including adding, updating, and removing samples associated with a study) can be done while offline. Those changes will be synced to the NMDC Submission Portal the next time you're online. **Please create your study or studies before going to an area where you will not have network access.** Due to a known bug, we also recommend adding one temporary sample to the study while online as well.

### Multiple users accessing a single study

The NMDC Submission Portal has long provided the ability for multiple users to manage a single study. This ability is reflected in the NMDC Field Notes app, where users have access to all of the same studies that they do on the NMDC Submission Portal. Here are some things we want you to keep in mind when working with shared studies in the NMDC Field Notes app.

* The NMDC Field Notes app provides a simplified interface for creating studies. **A study created via the app will initially only be accessible to you (as the creator) and the study’s Principal Investigator** if you provide an ORCID iD for the Principal Investigator that is not your own. If necessary, more collaborators can be added later via the NMDC Submission Portal.  
* Similar to the NMDC Submission Portal, the app allows only one person to modify a given study at a time in order to prevent conflicting updates. Therefore **you may see a warning in the app saying you cannot edit a study** (including adding, updating, and removing samples associated with the study) while it is being edited by another user.  
* If you use the app without a network connection, the app cannot know if a shared study is being edited by another user. It will allow you to make edits, and it will sync those edits with the server the next time you use the app while online. However, **this delayed sync may overwrite edits made by other users while you were offline**. If you plan on working in an area with limited or no network access, consider having each user work on separate studies and manually merging the separate studies together via the NMDC Submission Portal at a later time.

## How to provide feedback

**We would like to hear from you about any bugs, unexpected behavior, or ideas for improvements encountered while using the NMDC Field Notes app.**

If you have a GitHub account, we encourage you to submit a new issue here: [https://github.com/microbiomedata/nmdc-field-notes/issues/new/choose](https://github.com/microbiomedata/nmdc-field-notes/issues/new/choose). That will allow you to get the most direct updates on the issue from our team. You will also be able to submit screenshots here.

Otherwise, please use this Google Form to report an issue: [https://forms.gle/b1vW3JLTXZa62ooo6](https://forms.gle/b1vW3JLTXZa62ooo6).

| ℹ️ | Apple users will also see a link in the TestFlight app that says “Send Beta Feedback”. We encourage you to use either GitHub or the Google Form linked above to provide feedback instead of using this link. |
| ----: | :---- |

Finally, once you have completed any testing you would like to do, you are welcome to let us know at [support@microbiomedata.org](mailto:support@microbiomedata.org). We will send you another Google Form for you to share your overall impressions and your use cases.