import subprocess
urls = ["https://mooc.nthu.edu.tw:8888/Upload/Material/1926686a74b29060adb0cdc7aac7fe2b.pdf",
    "https://mooc.nthu.edu.tw:8888/Upload/Material/36995f015efd731451de3a9fe19463f4.pdf",
    "https://mooc.nthu.edu.tw:8888/Upload/Material/8fef29b82dfb642c7a5534cb9c8c5a05.pdf",
    "https://mooc.nthu.edu.tw:8888/Upload/Material/5f47d9df7c381c9016de9a7e7d68af02.pdf",
    "https://mooc.nthu.edu.tw:8888/Upload/Material/03c826a449687f210aefb76ea44155b0.pdf",
    "https://mooc.nthu.edu.tw:8888/Upload/Material/316e151163a9930a763c64e6ba07d4fe.pdf",
    "https://mooc.nthu.edu.tw:8888/Upload/Material/99ee3d269131b82bcd9bd26a3b8c9747.pdf",
    "https://mooc.nthu.edu.tw:8888/Upload/Material/45046c5f66cfa2488bfe22d0f1f28746.pdf",
    "https://mooc.nthu.edu.tw:8888/Upload/Material/501673cdaa554f28e124ad3991712d25.pdf",
    "https://mooc.nthu.edu.tw:8888/Upload/Material/ab42952dbaf6a8a18b0eeb8224f3139b.pdf",
    "https://mooc.nthu.edu.tw:8888/Upload/Material/fd19db56f9d71ac7e6cef3555625e60b.pdf",
    "https://mooc.nthu.edu.tw:8888/Upload/Material/1dc781f642995f71c43e60b08e897294.pdf",
    "https://mooc.nthu.edu.tw:8888/Upload/Material/cf7bf4284bb3ddf427e716ac6fb5300c.pdf",
    "https://mooc.nthu.edu.tw:8888/Upload/Material/54005b69cc73157873bd1ff6ce1e63f3.pdf",
    "https://mooc.nthu.edu.tw:8888/Upload/Material/2227221e9a21a50d43a91c49272b39e7.pdf",
    "https://mooc.nthu.edu.tw:8888/Upload/Material/ef680510509d7a9b3577d240a05e9497.pdf",
    "https://mooc.nthu.edu.tw:8888/Upload/Material/41060dba2ccefd67551199a4933340bf.pdf",
    "https://mooc.nthu.edu.tw:8888/Upload/Material/8a249bff0a8c42e2f06f7dbc381c20e3.pdf",
    "https://mooc.nthu.edu.tw:8888/Upload/Material/30aa7c49b33d0a8689823e5a7e70cc1b.pdf",
    "https://mooc.nthu.edu.tw:8888/Upload/Material/e7dac3c56ea3c934f8fcf12848fbffde.pdf",
    "https://mooc.nthu.edu.tw:8888/Upload/Material/c7d46224002faf0ab20c9ff0a992214d.pdf",
    "https://mooc.nthu.edu.tw:8888/Upload/Material/4c1668ef7c7aa3b17bb6aa2e46d35948.pdf",
    "https://mooc.nthu.edu.tw:8888/Upload/Material/f02b0eb12177be1f145f27bb0080e4b1.pdf",
    "https://mooc.nthu.edu.tw:8888/Upload/Material/2afed8af48fd2e127d3f4e78ec4c5958.pdf"
]

for i, url in enumerate(urls):
    command = ["curl", '-o', f"file{i+1}.pdf", url]
    response = subprocess.run(command)


