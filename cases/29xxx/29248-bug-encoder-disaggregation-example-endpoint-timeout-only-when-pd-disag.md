# vllm-project/vllm#29248: [Bug]: Encoder disaggregation example endpoint timeout (Only when PD disaggregation enabled)

| 字段 | 值 |
| --- | --- |
| Issue | [#29248](https://github.com/vllm-project/vllm/issues/29248) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Encoder disaggregation example endpoint timeout (Only when PD disaggregation enabled)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug [Commit used](https://github.com/vllm-project/vllm/commit/e9af6ba62ac99683139ff8d6bac87677fecf0b0c) I am using `examples/online_serving/disaggregated_encoder/disagg_1e1p1d_example.sh` ([link](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/disaggregated_encoder/disagg_1e1p1d_example.sh)) to run the new encoder disaggregation feature. After the service is up, the `vllm bench serve` just hang. I suspect it hang [here](https://github.com/vllm-project/vllm/blob/main/vllm/benchmarks/lib/ready_checker.py#L58). **However, another example script, `disagg_1e1pd_example.sh`, works well on my side.** Here is what I got. ```text $ GPU_E=0 GPU_PD=1 GPU_P=1 GPU_D=2 PROXY_PORT=10002 bash disagg_1e1p1d_example.sh remove previous ec cache folder make ec cache folder All services are up! Running benchmark (stream)... INFO 11-22 17:04:04 [scheduler.py:207] Chunked prefill is enabled with max_num_batched_tokens=2048. Namespace(subparser='bench', bench_type='serve', dispatch_function= , seed=0, num_prompts=100, dataset_name='hf', no_stream=False, dataset_path='lmarena-ai/VisionArena-Chat', no_oversample=False, skip_chat_templat...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: ype='serve', dispatch_function= , seed=0, num_prompts=100, dataset_name='hf', no_stream=False, dataset_path='lmarena-ai/VisionArena-Chat', no_oversample=False, skip_chat_template=False, disable_shuffle=False, custom_out...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: xamples/online_serving/disaggregated_encoder/disagg_1e1p1d_example.sh` ([link](https://github.com/vllm-project/vllm/blob/main/examples/online_serving/disaggregated_encoder/disagg_1e1p1d_example.sh)) to run the new encod...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ation example endpoint timeout (Only when PD disaggregation enabled) bug;stale ### Your current environment ### 🐛 Describe the bug [Commit used](https://github.com/vllm-project/vllm/commit/e9af6ba62ac99683139ff8d6bac876...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: um_batched_tokens=2048. Namespace(subparser='bench', bench_type='serve', dispatch_function= , seed=0, num_prompts=100, dataset_name='hf', no_stream=False, dataset_path='lmarena-ai/VisionArena-Chat', no_oversample=False,...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: atch_function= , seed=0, num_prompts=100, dataset_name='hf', no_stream=False, dataset_path='lmarena-ai/VisionArena-Chat', no_oversample=False, skip_chat_template=False, disable_shuffle=False, custom_output_len=256, spec...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
