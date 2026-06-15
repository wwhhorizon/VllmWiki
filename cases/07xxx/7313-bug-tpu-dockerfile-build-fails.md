# vllm-project/vllm#7313: [Bug]: TPU Dockerfile build fails

| 字段 | 值 |
| --- | --- |
| Issue | [#7313](https://github.com/vllm-project/vllm/issues/7313) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TPU Dockerfile build fails

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `docker build -f Dockerfile.tpu -t vllm-tpu .` fails on `main` branch (commit `5fb4a3f6785e3612bf1741f6e43a4184a37649c1`) and on tag `v0.5.4`: ``` #13 212.5 Installing huggingface_hub-0.24.5-py3-none-any.whl to /usr/local/lib/python3.10/site-packages #13 212.7 Adding huggingface-hub 0.24.5 to easy-install.pth file #13 212.7 Installing huggingface-cli script to /usr/local/bin #13 212.7 #13 212.7 Installed /usr/local/lib/python3.10/site-packages/huggingface_hub-0.24.5-py3.10.egg #13 212.7 error: tokenizers 0.20.0rc1 is installed but tokenizers =0.19 is required by {'transformers'} #13 ERROR: process "/bin/sh -c cd /workspace/vllm && python setup.py develop" did not complete successfully: exit code: 1 ------ > [9/9] RUN cd /workspace/vllm && python setup.py develop: 211.5 Reading https://pypi.org/simple/huggingface-hub/ 212.4 Downloading https://files.pythonhosted.org/packages/0b/05/31b21998f68c31e7ffcc27ff08531fb9af5506d765ce8d661fb0036e6918/huggingface_hub-0.24.5-py3-none-any.whl#sha256=d93fb63b1f1a919a22ce91a14518974e81fc4610bf344dfe7572343ce8d3aced 212.5 Best match: huggingface-hub 0.24.5 212.5 Processing huggingface_hub-0.24.5-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: TPU Dockerfile build fails bug ### Your current environment ### 🐛 Describe the bug `docker build -f Dockerfile.tpu -t vllm-tpu .` fails on `main` branch (commit `5fb4a3f6785e3612bf1741f6e43a4184a37649c1`) and on...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: f1741f6e43a4184a37649c1`) and on tag `v0.5.4`: ``` #13 212.5 Installing huggingface_hub-0.24.5-py3-none-any.whl to /usr/local/lib/python3.10/site-packages #13 212.7 Adding huggingface-hub 0.24.5 to easy-install.pth file...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
