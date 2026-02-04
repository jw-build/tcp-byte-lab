# 01-raw-bytes — TCP is a byte stream (no message boundaries)

## Goal
Observe that TCP delivers an unstructured byte stream:
- recv chunking is not equal to send chunking
- only byte order is preserved

## Payload
client payload (hex):
010268656c6c6fff

## Observations (server recv chunks)
recv #1: 010268
recv #2: 656c6c6f
recv #3: ff

concatenated:
010268656c6c6fff  == payload ✅

## Packet capture
tcpdump / wireshark shows TCP payload bytes containing:
01 02 68 65 6c 6c 6f ff
(possibly split across segments)
