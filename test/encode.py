import base64
url = 'https://docs.google.com/forms/d/e/1FAIpQLSdzeva4f_Im0LMJ01KQkWD_NbWSub4kqTK3_kDmKqwPpiqmCw/viewform?edit2=2_ABaOnuet3Ks0vOt_Ba4NuYOlYH2OzZ2PzB8Tfjz0U45dZXyCXLD4_ICSKdpRwlrQsI4esOs'

print(base64.urlsafe_b64encode(url.encode()))
