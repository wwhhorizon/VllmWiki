# vllm-project/vllm#29177: [Usage]: Vllm + Intervl model  local infra Image preprocessing / request adding becomes bottleneck even with more CPU cores — how to accelerate?

| 字段 | 值 |
| --- | --- |
| Issue | [#29177](https://github.com/vllm-project/vllm/issues/29177) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Vllm + Intervl model  local infra Image preprocessing / request adding becomes bottleneck even with more CPU cores — how to accelerate?

### Issue 正文摘录

### Your current environment vllm 0.11.0 ### How would you like to use vllm ### current phenomenon When doing **batched image classification** (64 images per batch) with InternVL3_5-1B, the bottleneck is clearly in the **"Adding requests"** phase (image preprocessing). Even after increasing CPU cores and setting `OMP_NUM_THREADS=16`, the preprocessing speed stays around **50 it/s**, while the actual generation phase is extremely fast (>1500 prompts/s). ```text Adding requests: 100%|██████████| 64/64 [00:01 \nYou are an image classifier. Output only one word: safe or nsfw." sampling_params = SamplingParams(temperature=0.0, max_tokens=8) batch_inputs = [] for i in range(64): img = Image.open(f"/path/to/images/{i}.jpg").convert("RGB") batch_inputs.append({ "prompt": prompt, "multi_modal_data": {"image": img}, }) outputs = llm.generate(batch_inputs, sampling_params=sampling_params, use_tqdm=True) ``` ### Expected behavior For pure-text batches, Adding requests is >2000 it/s such as qwen3vl. Attempted solutions (all ineffective) ### my attempt to speed up Increase CPU cores / set OMP_NUM_THREADS=16 → no speedup mm_processor_kwargs={"max_dynamic_patch": 1, ...} → seems no speedup Pre-re...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Vllm + Intervl model local infra Image preprocessing / request adding becomes bottleneck even with more CPU cores — how to accelerate? usage;stale ### Your current environment vllm 0.11.0 ### How would you like...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Vllm + Intervl model local infra Image preprocessing / request adding becomes bottleneck even with more CPU cores — how to accelerate? usage;stale ### Your current environment vllm 0.11.0 ### How would you like...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: eal ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. Thank you for the great work on vLLM! Looking forward to a simple way to slove it

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
