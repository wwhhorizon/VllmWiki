# vllm-project/vllm#27787: [Bug]: Under conditions of high concurrency, DeepSeek-V3.1 exhibits the phenomenon of generating nonsensical outputs when running on vllm 0.11.1rc4

| 字段 | 值 |
| --- | --- |
| Issue | [#27787](https://github.com/vllm-project/vllm/issues/27787) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Under conditions of high concurrency, DeepSeek-V3.1 exhibits the phenomenon of generating nonsensical outputs when running on vllm 0.11.1rc4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am testing DeepSeek's MTP, but I couldn't test it before the PR at https://github.com/vllm-project/vllm/pull/26541. Therefore, I copied the latest code, set ```TORCH_CUDA_ARCH_LIST=9.0``` on a ```4090D```, and executed ```pip install --editable .```. The editable version is ```vllm 0.11.1rc4.dev1+g29c9cb800 ```(git sha: 29c9cb800)，And package the vllm image compiled on the ```4090D```, then deploy it on the ```H200```. My startup command is: ```vllm serve /dsonline/models/DeepSeek-V3.1-Terminus --tensor-parallel-size 8 --served-model-name deepseek_v3_1 --enable-auto-tool-choice --tool-call-parser deepseek_v31 --max-num-seqs 1024 --reasoning-parser deepseek_v3 --trust-remote-code --max-model-len 131072``` When not using MTP parameters, I observe that when the batch size is relatively large, the model produces nonsensical outputs, leading to the KVCache being quite full. The test datasets are ordinary Chinese-to-English datasets and English abstract datasets. However, this phenomenon does not occur when the batch size is small (for the Chinese-to-English dataset, when ```batch size ≥ 320```; for the English abstract dataset, when...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: easoning-parser deepseek_v3 --trust-remote-code --max-model-len 131072 --speculative-config '{"method": "deepseek_mtp", "num_speculative_tokens": 2}' ``` It indicates that vllm's CUDA Graph optimization is incompatible...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: set ```TORCH_CUDA_ARCH_LIST=9.0``` on a ```4090D```, and executed ```pip install --editable .```. The editable version is ```vllm 0.11.1rc4.dev1+g29c9cb800 ```(git sha: 29c9cb800)，And package the vllm image compiled on...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=8, pipeline_parallel_size=1, data_parallel_siz...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ::detail::function_call&) File " ", line 0, in pybind11::cpp_function::dispatcher(_object*, _object*, _object*) File " ", line 0, in _PyObject_MakeTpCall File " ", line 0, in _PyEval_EvalFrameDefault File " ", line 0, i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: 1.1rc4 bug ### Your current environment ### 🐛 Describe the bug I am testing DeepSeek's MTP, but I couldn't test it before the PR at https://github.com/vllm-project/vllm/pull/26541. Therefore, I copied the latest code, s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
