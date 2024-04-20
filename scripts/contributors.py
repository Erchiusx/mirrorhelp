import os
import requests


HEADER = """\
# 文档贡献者名单

你也可以前往 <https://github.com/ustclug/mirrorhelp/graphs/contributors> 获取全部贡献者列表。

以字典序排序：
"""


def get_api():
    if "CI" not in os.environ:
        return [
            {
                "login": "（本文件由 CI 生成，参见仓库中的 `scripts/contributors.py`）"
            }
        ]
    headers = {
        "User-Agent": "Python/0.0.1 (+https://github.com/ustclug/mirrorhelp/blob/master/source/contributors.py)"
    }
    if "GITHUB_TOKEN" in os.environ:
        headers["Authorization"] = f"token {os.environ['GITHUB_TOKEN']}"
    r = requests.get("https://api.github.com/repos/ustclug/mirrorhelp/contributors", headers=headers)
    r.raise_for_status()
    return r.json()


def main():
    filename = os.path.abspath(os.path.join(__file__, os.path.pardir, os.path.pardir, "docs", "contributor.md"))
    with open(filename, "w") as f:
        print(HEADER, file=f)
        data = get_api()
        data.sort(key=lambda x: x["login"].casefold())
        for item in data:
            print(f"* {item['login']}", file=f)


if __name__ == "__main__":
    main()
