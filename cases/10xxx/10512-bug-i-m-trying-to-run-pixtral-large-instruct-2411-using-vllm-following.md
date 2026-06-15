# vllm-project/vllm#10512: [Bug]: I'm trying to run Pixtral-Large-Instruct-2411 using vllm, following the documentation at https://huggingface.co/mistralai/Pixtral-Large-Instruct-2411, but I encountered an error.

| 字段 | 值 |
| --- | --- |
| Issue | [#10512](https://github.com/vllm-project/vllm/issues/10512) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: I'm trying to run Pixtral-Large-Instruct-2411 using vllm, following the documentation at https://huggingface.co/mistralai/Pixtral-Large-Instruct-2411, but I encountered an error.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Command: 'vllm serve mistralai/Pixtral-Large-Instruct-2411 --config-format mistral --load-format mistral --tokenizer_mode mistral --limit_mm_per_prompt 'image=10' --tensor-parallel-size 8' Full Log: ubuntu@192-222-52-186:~$ vllm serve mistralai/Pixtral-Large-Instruct-2411 --config-format mistral --max-model-len 8192 --load-format mistral --tokenizer_mode mistral --limit_mm_per_prompt 'image=2' --tensor-parallel-size 8 2024-11-21 02:51:57.103583: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`. 2024-11-21 02:51:57.114316: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered 2024-11-21 02:51:57.127862: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one ha...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: l-Large-Instruct-2411 using vllm, following the documentation at https://huggingface.co/mistralai/Pixtral-Large-Instruct-2411, but I encountered an error. bug;stale ### Your current environment ### Model Input Dumps _No...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 12F AVX512_VNNI AVX512_BF16 AVX512_FP16 AVX_VNNI, in other operations, rebuild TensorFlow with the appropriate compiler flags. /usr/lib/python3/dist-packages/scipy/__init__.py:146: UserWarning: A NumPy version >=1.17.3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ations. To enable the following instructions: AVX512F AVX512_VNNI AVX512_BF16 AVX512_FP16 AVX_VNNI, in other operations, rebuild TensorFlow with the appropriate compiler flags. /usr/lib/python3/dist-packages/scipy/__ini...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: o/mistralai/Pixtral-Large-Instruct-2411, but I encountered an error. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Command: 'vllm serve mistralai/Pixtral-Large-Instruc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ib/python3.10/site-packages/vllm/scripts.py", line 195, in main args.dispatch_function(args) File "/home/ubuntu/.local/lib/python3.10/site-packages/vllm/scripts.py", line 41, in serve uvloop.run(run_server(args)) File "...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
