# vllm-project/vllm#30604: [Installation]: [ARM_CPU_backend]  Engine core proc EngineCore_DP0 died unexpectedly, shutting down client.

| 字段 | 值 |
| --- | --- |
| Issue | [#30604](https://github.com/vllm-project/vllm/issues/30604) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: [ARM_CPU_backend]  Engine core proc EngineCore_DP0 died unexpectedly, shutting down client.

### Issue 正文摘录

I failed to install vLLM from the source with vllm's document. Instead, I install vLLM from the source with the document (https://learn.arm.com/learning-paths/servers-and-cloud-computing/vllm/vllm-setup/). The target ARM server is a AWS r7g.2xlarge instance (64GRAM, 8cores) using Graviton 3 ARM CPU. I need to develop third party library for vLLM, and will modify the source code of vLLM, thus i need to install vllm from source. I run the following test.py code: ``` from vllm import LLM if __name__ == "__main__": llm = LLM(model="facebook/opt-125m") ``` I run the code with the following command: > export VLLM_CPU_KVCACHE_SPACE=40 > export VLLM_CPU_NUM_OF_RESERVED_CPU=1 > python test.py ### The output of the above code is: ``` INFO 12-13 09:20:04 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available. INFO 12-13 09:20:05 [utils.py:253] non-default args: {'seed': None, 'disable_log_stats': True, 'model': 'facebook/opt-125m'} WARNING 12-13 09:20:05 [arg_utils.py:1209] `seed=None` is equivalent to `seed=0` in V1 Engine. You will no longer be allowed to pass `None` in v0.13. INFO 12-13 09:20:06 [model.py:629] Resolved architecture: O...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: [ARM_CPU_backend] Engine core proc EngineCore_DP0 died unexpectedly, shutting down client. installation I failed to install vLLM from the source with vllm's document. Instead, I install vLLM from the so
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: wed to pass `None` in v0.13. INFO 12-13 09:20:06 [model.py:629] Resolved architecture: OPTForCausalLM INFO 12-13 09:20:06 [model.py:1755] Using max model len 2048 INFO 12-13 09:20:06 [scheduler.py:228] Chunked prefill i...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 3 09:20:06 [model.py:1755] Using max model len 2048 INFO 12-13 09:20:06 [scheduler.py:228] Chunked prefill is enabled with max_num_batched_tokens=4096. INFO 12-13 09:20:12 [importing.py:68] Triton not installed or not c...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Installation]: [ARM_CPU_backend] Engine core proc EngineCore_DP0 died unexpectedly, shutting down client. installation I failed to install vLLM from the source with vllm's document. Instead, I install vLLM from the sou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
