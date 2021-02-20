#NoEnv  ;
; #Warn 
SendMode Input
SetWorkingDir %A_ScriptDir% 

F8::Pause    ; F8 to pause the script
;F10::Suspend  ; F10 to Suspend - wont stop spamming, will pause the sript after spamming (you can pause and then suspend, it will work)
F9::Reload   ; F9 to reload the script, everything done by the script will stop and restarted

^!0:: ; ctrl+alt+0
InputBox, word, Input the Name, Please enter the message you wan't to SPAM, ,290,200
InputBox, number, Input the Number, Please enter the number of messages you wan't to SPAM, ,290,200
InputBox, latime, Input the Delay of Spam, Please keep this number above 80. Enter the number in "ms", ,290,200
Loop, %number%
{
Send, %word%
SendInput {Return}
Sleep, %latime%
}
MsgBox, Done! -make sure to check out my other scripts! -Created by Hirusha Adikari Thank You!

