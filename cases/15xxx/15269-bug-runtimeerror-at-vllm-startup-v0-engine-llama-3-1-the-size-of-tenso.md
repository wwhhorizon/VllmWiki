# vllm-project/vllm#15269: [Bug]: RuntimeError at vllm startup, V0 engine, Llama 3.1, "The size of tensor a (50) must match the size of tensor b (56) at non-singleton dimension 0"

| 字段 | 值 |
| --- | --- |
| Issue | [#15269](https://github.com/vllm-project/vllm/issues/15269) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError at vllm startup, V0 engine, Llama 3.1, "The size of tensor a (50) must match the size of tensor b (56) at non-singleton dimension 0"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Model is `meta-llama/Llama-3.1-8B-Instruct`. The issue was absent on VLLM 0.7.2. VLLM is being run with `VLLM_USE_V1=0` to force V0 inference engine. VLLM crashes during cuda graph capture. Last successfully logged message: ``` (VllmWorkerProcess pid=1283553) INFO 03-21 04:33:32 [model_runner.py:1442] Capturing cudagraphs for decoding. This may lead to unexpected consequences if t he model is not static. To run the model in eager mode, set 'enforce_eager=True' or use '--enforce-eager' in the CLI. If out-of-memory error occurs during cudagraph capture, consider decreasing `gpu_memory_utilization` or switching to eager mode. You can also reduce the `max_num_seqs` as needed to decrease me mory usage. INFO 03-21 04:33:32 [model_runner.py:1442] Capturing cudagraphs for decoding. This may lead to unexpected consequences if the model is not static. To run t he model in eager mode, set 'enforce_eager=True' or use '--enforce-eager' in the CLI. If out-of-memory error occurs during cudagraph capture, consider decr easing `gpu_memory_utilization` or switching to eager mode. You can also reduce the `max_num_seqs` as needed to decrease memory...

## 现有链接修复摘要

#15308 [Bugfix] LoRA V0 - Fix case where `max_num_seqs` is between cudagraph capture sizes

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: with `VLLM_USE_V1=0` to force V0 inference engine. VLLM crashes during cuda graph capture. Last successfully logged message: ``` (VllmWorkerProcess pid=1283553) INFO 03-21 04:33:32 [model_runner.py:1442] Capturing cudag...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: r.py", line 1509, in capture_model self.set_active_loras(set(), lora_mapping) File "/home/shadeform/precog/.venv/lib/python3.12/site-packages/vllm/worker/model_runner.py", line 1371, in set_active_loras self.lora_manage...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: RuntimeError at vllm startup, V0 engine, Llama 3.1, "The size of tensor a (50) must match the size of tensor b (56) at non-singleton dimension 0" bug ### Your current environment ### 🐛 Describe the bug Model is `...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 1371, in set_active_loras self.lora_manager.set_active_adapters(lora_requests, lora_mapping) File "/home/shadeform/precog/.venv/lib/python3.12/site-packages/vllm/lora/worker_manager.py", line 167, in set_active_adapters...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#15308](https://github.com/vllm-project/vllm/pull/15308) | closes_keyword | 0.95 | [Bugfix] LoRA V0 - Fix case where `max_num_seqs` is between cudagraph capture sizes | FIX #15269 Repro command : ``` VLLM_USE_V1=0 python3 benchmarks/benchmark_throughput.py --model meta-llama/Llama-2-7b-hf --backend vllm --dataset ./ShareGPT_V3_unfiltered_cleaned |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
