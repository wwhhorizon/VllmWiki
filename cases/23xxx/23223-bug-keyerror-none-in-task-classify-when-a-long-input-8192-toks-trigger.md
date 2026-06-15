# vllm-project/vllm#23223: [Bug]: KeyError: None in task="classify" when a long input (>8192 toks) triggers chunked prefill with max_num_seqs>1 (vLLM 0.10.1)

| 字段 | 值 |
| --- | --- |
| Issue | [#23223](https://github.com/vllm-project/vllm/issues/23223) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KeyError: None in task="classify" when a long input (>8192 toks) triggers chunked prefill with max_num_seqs>1 (vLLM 0.10.1)

### Issue 正文摘录

### 🐛 Describe the bug ### Summary LLM.classify(...) crashes with KeyError: None whenever a long example exceeds the default `max_num_batched_tokens` (8192) and triggers chunked prefill, but only when `max_num_seqs >= 2`. It succeeds with `max_num_seqs=1`. ### Repro (minimal) ``` from vllm import LLM # texts contains many short items + one very long string (> 8192 tokens) llm = LLM( model=model_path, task="classify", trust_remote_code=True, gpu_memory_utilization=0.9, max_num_seqs=8, # fails for 4/8/16; works for 1 (sometimes 2) ) res = llm.classify(texts) # vLLM logs: "Chunked prefill enabled with max_num_batched_tokens=8192" ``` ### Observed ``` ... vllm/v1/worker/gpu_model_runner.py", line 712, in _prepare_inputs tokens = [scheduler_output.num_scheduled_tokens[i] for i in req_ids] KeyError: None ``` ### Expected No crash when chunked prefill occurs; or a clear error if limits are exceeded. ### Environment vLLM 0.10.1 (pip), Python 3.12 Model: llama-3.1–based RM (`task="classify", trust_remote_code=True`) GPU/CUDA/PyTorch: A100, CUDA 12.2, PyTorch 2.7.1 ### Workarounds Set `max_num_seqs=1` (stable) Truncate long inputs to ≤8192 tokens Potential: raise `max_num_batched_tokens` ab...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: `. It succeeds with `max_num_seqs=1`. ### Repro (minimal) ``` from vllm import LLM # texts contains many short items + one very long string (> 8192 tokens) llm = LLM( model=model_path, task="classify", trust_remote_code...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: del: llama-3.1–based RM (`task="classify", trust_remote_code=True`) GPU/CUDA/PyTorch: A100, CUDA 12.2, PyTorch 2.7.1 ### Workarounds Set `max_num_seqs=1` (stable) Truncate long inputs to ≤8192 tokens Potential: raise `m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: None in task="classify" when a long input (>8192 toks) triggers chunked prefill with max_num_seqs>1 (vLLM 0.10.1) bug ### 🐛 Describe the bug ### Summary LLM.classify(...) crashes with KeyError: None whenever a long exam...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: s many short items + one very long string (> 8192 tokens) llm = LLM( model=model_path, task="classify", trust_remote_code=True, gpu_memory_utilization=0.9, max_num_seqs=8, # fails for 4/8/16; works for 1 (sometimes 2) )...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.7.1 [pip3] torchvision==0.22.1 [pip3] transformers==4.55.2 [pip3] triton==3.3.1 [conda] numpy 2.1.2 pypi_0 pypi [conda] nvidia-cublas-cu12 12.6.4.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.6.80

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
