# vllm-project/vllm#11542: [Installation]: No matching distribution found for xgrammar>=0.1.6; platform_machine == "x86_64"

| 字段 | 值 |
| --- | --- |
| Issue | [#11542](https://github.com/vllm-project/vllm/issues/11542) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: No matching distribution found for xgrammar>=0.1.6; platform_machine == "x86_64"

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` I got this error. ### How you are installing vllm I download the latest .whl from [vllm-0.6.6+cu118-cp38-abi3-manylinux1_x86_64.whl](https://github.com/vllm-project/vllm/releases/download/v0.6.6/vllm-0.6.6+cu118-cp38-abi3-manylinux1_x86_64.whl). The problem I face: ```sh pip install vllm-0.6.6+cu118-cp38-abi3-manylinux1_x86_64.whl Processing ./vllm-0.6.6+cu118-cp38-abi3-manylinux1_x86_64.whl Requirement already satisfied: psutil in ~/anaconda3/envs/llmeval/lib/python3.10/site-packages (from vllm==0.6.6+cu118) (6.1.0) Requirement already satisfied: sentencepiece in ~/anaconda3/envs/llmeval/lib/python3.10/site-packages (from vllm==0.6.6+cu118) (0.2.0) Requirement already satisfied: numpy =2.26.0 in ~/anaconda3/envs/llmeval/lib/python3.10/site-packages (from vllm==0.6.6+cu118) (2.32.3) Requirement already satisfied: tqdm in ~/anaconda3/envs/llmeval/lib/python3.10/site-packages (from vllm==0.6.6+cu118) (4.67.1) Collecting blake3 (from vllm==0.6.6+cu118) Using cached blake3-1.0.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.1 kB) Requirement already satisfied: py-cpuinfo in ~/anacon...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: No matching distribution found for xgrammar>=0.1.6; platform_machine == "x86_64" installation ### Your current environment ```text The output of `python collect_env.py` ``` I got this error. ### How y
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: I got this error. ### How you are installing vllm I download the latest .whl from [vllm-0.6.6+cu118-cp38-abi3-manylinux1_x86_64.whl](https://github.com/vllm-project/vllm/releases/download/v0.6.6/vllm-0.6.6+cu118-cp38-ab...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: blake3-1.0.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.1 kB) Requirement already satisfied: py-cpuinfo in ~/anaconda3/envs/llmeval/lib/python3.10/site-packages (from vllm==0.6.6+cu118) (9.0....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: kages (from vllm==0.6.6+cu118) (0.7.0) Requirement already satisfied: lm-format-enforcer =0.10.9 in ~/anaconda3/envs/llmeval/lib/python3.10/site-packages (from vllm==0.6.6+cu118) (0.10.9) Collecting outlines==0.1.11 (fr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
