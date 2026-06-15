# vllm-project/vllm#16987: [Bug]: `original_load_name` undefined with certain torch versions

| 字段 | 值 |
| --- | --- |
| Issue | [#16987](https://github.com/vllm-project/vllm/issues/16987) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `original_load_name` undefined with certain torch versions

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug My issue is with the if-elif block on Lines 199 -249 of [compiler_interface.py](https://github.com/vllm-project/vllm/blob/5b1aca2ae39b4bcdd04d916ec55bfc87f98d4835/vllm/compilation/compiler_interface.py#L199), which depends on the torch version. But because of how [pytorch.torch_version.TorchVersion](https://github.com/pytorch/pytorch/blob/main/torch/torch_version.py) is defined, non-standard torch versions like mine (which was **2.6.0a0+ecf3bae40a.nv25.01**) fail both the if and elif clauses, see: ``` >>> import torch >>> torch.__version__ '2.6.0a0+ecf3bae40a.nv25.01' >>> torch.__version__ >= "2.6" False ``` This led to certain variables like `original_load_name` not getting defined, and then problems with loading models via vllm. Here is the Dockerfile for the environment in which vLLM and this alpha version of torch was installed: ``` FROM nvcr.io/nvidia/pytorch:25.01-py3 WORKDIR /workdir RUN git clone https://github.com/vllm-project/vllm.git WORKDIR /workdir/vllm RUN python use_existing_torch.py RUN pip install -r requirements/build.txt RUN pip install -v -e . --no-build-isolation ``` Finally, here below is what a friend and I...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: `original_load_name` undefined with certain torch versions bug ### Your current environment ### 🐛 Describe the bug My issue is with the if-elif block on Lines 199 -249 of [compiler_interface.py](https://github.co...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ent environment ### 🐛 Describe the bug My issue is with the if-elif block on Lines 199 -249 of [compiler_interface.py](https://github.com/vllm-project/vllm/blob/5b1aca2ae39b4bcdd04d916ec55bfc87f98d4835/vllm/compilation/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: er` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: `original_load_name` not getting defined, and then problems with loading models via vllm. Here is the Dockerfile for the environment in which vLLM and this alpha version of torch was installed: ``` FROM nvcr.io/nvidia/p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
