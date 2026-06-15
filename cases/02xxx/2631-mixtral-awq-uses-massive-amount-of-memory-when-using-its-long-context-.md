# vllm-project/vllm#2631: Mixtral AWQ uses massive amount of memory when using its long context, GPU OOM for 2*A100 80GB while normal Mixtral has no issues.

| 字段 | 值 |
| --- | --- |
| Issue | [#2631](https://github.com/vllm-project/vllm/issues/2631) |
| 状态 | closed |
| 标签 |  |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Mixtral AWQ uses massive amount of memory when using its long context, GPU OOM for 2*A100 80GB while normal Mixtral has no issues.

### Issue 正文摘录

vllm 0.2.7 with cuda 12.1. ``` python -m vllm.entrypoints.openai.api_server --port=5002 --host=0.0.0.0 --model=TheBloke/dolphin-2.7-mixtral-8x7b-AWQ --seed 1234 --trust-remote-code --quantization awq --tensor-parallel-size=2 ``` 2*A100 80GB, but when using longer context like filling 31k (leaving 1k for output), leads to GPU OOM. nvidia-smi shows using about 76GB per GPU up to that point. Makes AWQ in vLLM totally useless, since normal non-AWQ Mixtral works perfectly fine for exact same usage pattern. [awq.txt](https://github.com/vllm-project/vllm/files/14074288/awq.txt) I understand that if context is large that dominates GPU memory usage, but it can't be more than 16-bit model.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: uses massive amount of memory when using its long context, GPU OOM for 2*A100 80GB while normal Mixtral has no issues. vllm 0.2.7 with cuda 12.1. ``` python -m vllm.entrypoints.openai.api_server --port=5002 --host=0.0.0...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: xtral AWQ uses massive amount of memory when using its long context, GPU OOM for 2*A100 80GB while normal Mixtral has no issues. vllm 0.2.7 with cuda 12.1. ``` python -m vllm.entrypoints.openai.api_server --port=5002 --...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: istributed_parallel;model_support;quantization cuda;quantization oom env_dependency vllm 0.2.7 with cuda 12.1.
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: xtral-8x7b-AWQ --seed 1234 --trust-remote-code --quantization awq --tensor-parallel-size=2 ``` 2*A100 80GB, but when using longer context like filling 31k (leaving 1k for output), leads to GPU OOM. nvidia-smi shows usin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s.openai.api_server --port=5002 --host=0.0.0.0 --model=TheBloke/dolphin-2.7-mixtral-8x7b-AWQ --seed 1234 --trust-remote-code --quantization awq --tensor-parallel-size=2 ``` 2*A100 80GB, but when using longer context lik...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
