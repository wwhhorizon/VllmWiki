# vllm-project/vllm#43847: [Installation]: add wheel for vllm==0.21+cu129 with manylinux_2_24_x86_64

| 字段 | 值 |
| --- | --- |
| Issue | [#43847](https://github.com/vllm-project/vllm/issues/43847) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: add wheel for vllm==0.21+cu129 with manylinux_2_24_x86_64

### Issue 正文摘录

I use python 3.14, and these are the only wheels that are published. There is support for manylinux_2_24_x86_64 with cuda 13, can we have it for cuda 12.9 ? ie. having the wheel : `vllm-0.21.0+cu129-cp38-abi3-manylinux_2_24_x86_64.whl` if it's not worth it, is it possible to show me how to build this specific version from source? ### How you are installing vllm ```sh uv pip install vllm --extra-index-url https://wheels.vllm.ai/0.21.0/cu129 --extra-index-url https://download.pytorch.org/whl/cu129 --index-strategy unsafe-best-match ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: add wheel for vllm==0.21+cu129 with manylinux_2_24_x86_64 installation I use python 3.14, and these are the only wheels that are published. There is support for manylinux_2_24_x86_64 with cuda 13, can
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: that are published. There is support for manylinux_2_24_x86_64 with cuda 13, can we have it for cuda 12.9 ? ie. having the wheel : `vllm-0.21.0+cu129-cp38-abi3-manylinux_2_24_x86_64.whl` if it's not worth it, is it poss...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda build_error env_dependency I use python 3.14, and these are...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
