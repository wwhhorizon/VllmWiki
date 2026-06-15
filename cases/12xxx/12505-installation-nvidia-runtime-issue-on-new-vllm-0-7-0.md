# vllm-project/vllm#12505: [Installation]: Nvidia runtime issue? On new VLLM 0.7.0

| 字段 | 值 |
| --- | --- |
| Issue | [#12505](https://github.com/vllm-project/vllm/issues/12505) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Nvidia runtime issue? On new VLLM 0.7.0

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` docker run --runtime nvidia --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface -p 8000:8000 --ipc=host -e VLLM_ENABLE_PREFIX_CACHING=true --name qwen2.5_20250128 vllm/vllm-openai:v0.7.0 --model Qwen/Qwen2.5-72B-Instruct --tensor-parallel-size=4 --gpu-memory-utilization=0.90 --enforce-eager --rope-scaling '{"type": "yarn","factor": 4,"original_max_position_embeddings": 32768}' error: /usr/bin/ld: cannot find -lcuda: No such file or directory ### How you are installing vllm docker ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: collect_env.py` ``` docker run --runtime nvidia --gpus all -v ~/.cache/huggingface:/root/.cache/huggingface -p 8000:8000 --ipc=host -e VLLM_ENABLE_PREFIX_CACHING=true --name qwen2.5_20250128 vllm/vllm-openai:v0.7.0 --mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: Nvidia runtime issue? On new VLLM 0.7.0 installation ### Your current environment ```text The output of `python collect_env.py` ``` docker run --runtime nvidia --gpus all -v ~/.cache/huggingface:/root/.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: inal_max_position_embeddings": 32768}' error: /usr/bin/ld: cannot find -lcuda: No such file or directory ### How you are installing vllm docker ### Before submitting a new issue... - [x] Make sure you already searched f...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
