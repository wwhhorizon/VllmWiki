# vllm-project/vllm#11468: [Misc]: Molmo inference multi-GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#11468](https://github.com/vllm-project/vllm/issues/11468) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Molmo inference multi-GPU

### Issue 正文摘录

### Anything you want to discuss about vllm. Hello! I'm trying to run `allenai/Molmo-7B-D-0924` model using vllm, it works on a single GPU A100 80Gb, but it's very slow. I've tried to set `tensor_parallel_size=2` to use my 2 GPUs A100 80Gb and speedup inference, but I'm getting error `[rank0]: RuntimeError: Inplace update to inference tensor outside InferenceMode is not allowed.You can make a clone to get a normal tensor before doing inplace update.See https://github.com/pytorch/rfcs/pull/17 for more details.` ```python llm = LLM( model="allenai/Molmo-7B-D-0924", trust_remote_code=True, dtype="bfloat16", enforce_eager=False, enable_prefix_caching=True, tensor_parallel_size=2, ) sampling_params = SamplingParams( temperature=0.1, max_tokens=128, ) template = { "prompt": "my prompt", "multi_modal_data": { "image": Image.open(path).convert("RGB") }, } queries = [template, template] outputs = model.generate(queries, sampling_params=sampling_params, use_tqdm=True) ``` Also I have a question about performance, I've got these numbers `est. speed input: 9020.32 toks/s, output: 146.08 toks/s` and I feel like it should be faster... maybe I'm just using it in a wrong way. ### Before submittin...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: LM( model="allenai/Molmo-7B-D-0924", trust_remote_code=True, dtype="bfloat16", enforce_eager=False, enable_prefix_caching=True, tensor_parallel_size=2, ) sampling_params = SamplingParams( temperature=0.1, max_tokens=128...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: run `allenai/Molmo-7B-D-0924` model using vllm, it works on a single GPU A100 80Gb, but it's very slow. I've tried to set `tensor_parallel_size=2` to use my 2 GPUs A100 80Gb and speedup inference, but I'm getting error...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ", trust_remote_code=True, dtype="bfloat16", enforce_eager=False, enable_prefix_caching=True, tensor_parallel_size=2, ) sampling_params = SamplingParams( temperature=0.1, max_tokens=128, ) template = { "prompt": "my pro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: discuss about vllm. Hello! I'm trying to run `allenai/Molmo-7B-D-0924` model using vllm, it works on a single GPU A100 80Gb, but it's very slow. I've tried to set `tensor_parallel_size=2` to use my 2 GPUs A100 80Gb and...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: Molmo inference multi-GPU stale ### Anything you want to discuss about vllm. Hello! I'm trying to run `allenai/Molmo-7B-D-0924` model using vllm, it works on a single GPU A100 80Gb, but it's very slow. I've trie...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
