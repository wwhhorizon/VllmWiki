# vllm-project/vllm#25032: [Bug]: CUDA Illegal Memory access errors when running Qwen3-Next

| 字段 | 值 |
| --- | --- |
| Issue | [#25032](https://github.com/vllm-project/vllm/issues/25032) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA Illegal Memory access errors when running Qwen3-Next

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm seeing an issue with qwen3-next where using the vllm serve command `vllm serve Qwen/Qwen3-Next --tensor-parallel-size 4 --tool-call-parser hermes --enable-auto-tool-choice` -- sending concurrent requests with different large input + max_token output lengths (both >3000-4000) triggers an illegal memory access almost always. - Sometimes it happens even at concurrency 1 under sustained load. Similarly, any time I specify a small value for `max_num_seqs` (such as 4) I run into a similar Illegal memory access error. - Using MTP spec decoding almost always triggers this as well at low values of max-num-seqs and input tokens (<1500). ``` (EngineCore_DP0 pid=1470235) ERROR 09-17 04:06:37 [dump_input.py:69] Dumping input data for V1 LLM engine (v0.10.3.dev108+ga14b5d87d.d20250917) with config: model='/opt/dlami/nvme/models/Qwen3-Next', speculative_config=SpeculativeConfig(method='qwen3_next_mtp', model='/opt/dlami/nvme/models/Qwen3-Next', num_spec_tokens=5), tokenizer='/opt/dlami/nvme/models/Qwen3-Next', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat1...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: tool-call-parser hermes --enable-auto-tool-choice` -- sending concurrent requests with different large input + max_token output lengths (both >3000-4000) triggers an illegal memory access almost always. - Sometimes it h...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ens even at concurrency 1 under sustained load. Similarly, any time I specify a small value for `max_num_seqs` (such as 4) I run into a similar Illegal memory access error. - Using MTP spec decoding almost always trigge...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=262144, download_dir=None, load_format=auto, tensor_parallel_size=4, pipeline_parallel_size=1, data_parallel_siz...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: CUDA Illegal Memory access errors when running Qwen3-Next bug ### Your current environment ### 🐛 Describe the bug I'm seeing an issue with qwen3-next where using the vllm serve command `vllm serve Qwen/Qwen3-Next...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: CUDA Illegal Memory access errors when running Qwen3-Next bug ### Your current environment ### 🐛 Describe the bug I'm seeing an issue with qwen3-next where using the vllm serve command `vllm serve Qwen/Qwen3-Next...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
