# vllm-project/vllm#7588: [Bug]: p2p check in custom all reduce not working

| 字段 | 值 |
| --- | --- |
| Issue | [#7588](https://github.com/vllm-project/vllm/issues/7588) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: p2p check in custom all reduce not working

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug It seems the GPU P2P check script in `custom_all_reduce_utils.py` has trouble finding the cuda runtime; after some boot-up logic, vLLM CLI fails shortly with the error message `AssertionError: libcudart.so is not loaded in the current process`. It raises regardless of the GPU topology (whether NVX or PCIe, I mean) and vLLM server runs well with adding `--enable-custom-all-reduce=False` option or manually creating the `~/.cache/vllm/gpu_p2p_access_cache_for_0,1.json` cache file, so I think the current library search method in `gpu_p2p_access_check` should be updated somehow. The CLI arguments I used is as follow: ```bash vllm serve /mnt/model-vol-1/model/META-LLAMA-3.1-70B-INSTRUCT/ --port 8080 --root-path /notebook/cjackal/cjackal-vscode/proxy/8080 --served-model-name meta-llama/meta-llama-3.1-70b-instruct --quantization fp8 --tensor-parallel-size 2 ``` cf. there's another open issue about P2P check #3688 but it doesn't look relevant. full vLLM CLI log and traceback ``` INFO 08-16 11:21:48 api_server.py:339] vLLM API server version 0.5.4 INFO 08-16 11:21:48 api_server.py:340] args: Namespace(model_tag='/mnt/model-vol-1/model/META...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, num_speculative_tokens=None, speculative_draft_tensor_parallel_si...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: /proxy/8080 --served-model-name meta-llama/meta-llama-3.1-70b-instruct --quantization fp8 --tensor-parallel-size 2 ``` cf. there's another open issue about P2P check #3688 but it doesn't look relevant. full vLLM CLI log...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ent process`. It raises regardless of the GPU topology (whether NVX or PCIe, I mean) and vLLM server runs well with adding `--enable-custom-all-reduce=False` option or manually creating the `~/.cache/vllm/gpu_p2p_access...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: omehow. The CLI arguments I used is as follow: ```bash vllm serve /mnt/model-vol-1/model/META-LLAMA-3.1-70B-INSTRUCT/ --port 8080 --root-path /notebook/cjackal/cjackal-vscode/proxy/8080 --served-model-name meta-llama/me...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=2, max_parallel_loadin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
