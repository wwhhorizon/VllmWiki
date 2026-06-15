# vllm-project/vllm#38107: [Bug]: Abnormally bad performance on AMD ROCM gfx1030 (W6800, V620, 6900XT 6800XT)

| 字段 | 值 |
| --- | --- |
| Issue | [#38107](https://github.com/vllm-project/vllm/issues/38107) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Abnormally bad performance on AMD ROCM gfx1030 (W6800, V620, 6900XT 6800XT)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Performance on AMD gfx1030 is abmnormally bad. This GPU using llama.cpp or kobold.cpp will easily do in the tens of tokens/s generation speed not single digits as with vllm here. While I know these generation GPUs don't have dedicated tensor units, I don't think the performance should be this bad. Trying to understand why the performance is so bad with vllm only. Vllm and triton rocm are installed from source following the install steps in the vllm docs. No errors during build or install using ROCm 7.2.0. Here is the result of running Qwen3-8B on 2xAMD Radeon Pro V620 32GB: Start command: ``` vllm serve /home/arli/models/Qwen3-8B \ --gpu-memory-utilization 0.9 --max-model-len 32768 --port 8000 \ --max-num-seqs 16 -tp 2 \ --attention-backend TRITON_ATTN \ --served-model-name test ``` API call: ``` { "model": "test", "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Tell me a very very long story."} ], "temperature": 1.0, "max_tokens": 8192, "stream": false, "top_p": 0.95, "top_k": 20, "min_p": 0.0, "presence_penalty": 0.0, "repetition_penalty": 1.0 } ``` Output: ``` (vllm-amd...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: why the performance is so bad with vllm only. Vllm and triton rocm are installed from source following the install steps in the vllm docs. No errors during build or install using ROCm 7.2.0. Here is the result of runnin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: e the bug Performance on AMD gfx1030 is abmnormally bad. This GPU using llama.cpp or kobold.cpp will easily do in the tens of tokens/s generation speed not single digits as with vllm here. While I know these generation...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: .1.dev15181+g2e67fa756) with config: model='/home/arli/models/Qwen3-8B', speculative_config=None, tokenizer='/home/arli/models/Qwen3-8B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: um-seqs 16 -tp 2 \ --attention-backend TRITON_ATTN \ --served-model-name test ``` API call: ``` { "model": "test", "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content":...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=2, pipeline_parallel_size=1, data_parallel_size...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
