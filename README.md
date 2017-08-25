# Steganography
This is a demonstration for a computer security class.
I am not responsible for anything you do with it. I simply wrote this as an educational tool for myself.
For the time being it only works with images that are in a **lossless, RGB format**.

# Examples
This uses Python 3.
## Injecting Text Into an Image

This will inject the contents of `malware.sh` into `image.bmp`, and save the output as `injected.bmp`. The result is visually noticeable.

```bash
./inject.py image.bmp malware.sh injected.bmp
```

## Retrieving Text

This will subtract the pixel values of `image.bmp` and `injected.bmp` and write the difference to standard output. Essentially you should be able to retrieve the text you had originally injected.

```bash
./subtract.py image.bmp injeted.bmp
```

# Moral of the Story
Be careful when copy-pasting scripts from the internet. They could be malicious. Always avoid piping directly to bash when you have not directly read the script.

## Example
Theoretically, an attacker could ask you to do something like this (Don't do it unless you know what you are about to run!):

```bash
./subtract.py image.bmp injected.bmp | bash
```

