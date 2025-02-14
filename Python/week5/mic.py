import speech_recognition as sr

for (
    ind,
    name,
) in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Microphone: [{name}] found for Microphone(device_index={ind})")
