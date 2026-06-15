# vllm-project/vllm#9419: [Bug]: After 0.6.2 update to 0.6.3, INT8(W8A8) format cannot be loaded at all. No compiled cutlass_scaled_mm for a compute capability less than CUDA device capability: 75

| 字段 | 值 |
| --- | --- |
| Issue | [#9419](https://github.com/vllm-project/vllm/issues/9419) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: After 0.6.2 update to 0.6.3, INT8(W8A8) format cannot be loaded at all. No compiled cutlass_scaled_mm for a compute capability less than CUDA device capability: 75

### Issue 正文摘录

### Your current environment ### Model Input Dumps [err_execute_model_input_20241016-194444.zip](https://github.com/user-attachments/files/17395135/err_execute_model_input_20241016-194444.zip) ### 🐛 Describe the bug As the title says, after upgrading from 0.6.2 to 0.6.3, I can't load the W8A8 format model in my WSL2 environment: ``` (base) root@DESKTOP-PEPA2G9:/mnt/c/Windows/system32# python3 -m vllm.entrypoints.openai.api_server --model /mnt/e/Code/models/Orca-2-13b-W8A8 --max-model-len 4096 --tensor-parallel-size 2 --gpu-memory-utilization 0.73 --dtype=half /root/miniconda3/lib/python3.12/site-packages/vllm/connections.py:8: RuntimeWarning: Failed to read commit hash: No module named 'vllm._version' from vllm.version import __version__ as VLLM_VERSION INFO 10-16 19:41:34 api_server.py:528] vLLM API server version dev INFO 10-16 19:41:34 api_server.py:529] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: e, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ter 0.6.2 update to 0.6.3, INT8(W8A8) format cannot be loaded at all. No compiled cutlass_scaled_mm for a compute capability less than CUDA device capability: 75 bug ### Your current environment ### Model Input Dumps [e...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: to 0.6.3, INT8(W8A8) format cannot be loaded at all. No compiled cutlass_scaled_mm for a compute capability less than CUDA device capability: 75 bug ### Your current environment ### Model Input Dumps [err_execute_model_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: update to 0.6.3, INT8(W8A8) format cannot be loaded at all. No compiled cutlass_scaled_mm for a compute capability less than CUDA device capability: 75 bug ### Your current environment ### Model Input Dumps [err_execute...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: mat cannot be loaded at all. No compiled cutlass_scaled_mm for a compute capability less than CUDA device capability: 75 bug ### Your current environment ### Model Input Dumps [err_execute_model_input_20241016-194444.zi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
