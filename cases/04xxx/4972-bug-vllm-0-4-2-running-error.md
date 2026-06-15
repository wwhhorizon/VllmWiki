# vllm-project/vllm#4972: [Bug]:vllm-0.4.2 running error 

| 字段 | 值 |
| --- | --- |
| Issue | [#4972](https://github.com/vllm-project/vllm/issues/4972) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error;crash;import_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:vllm-0.4.2 running error 

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug compile steps： 1. pip install -r requirements-build.txt ；pip install -r requirements-dev.txt ；pip install -r requirements-common.txt ；pip install -r requirements-cuda.txt ； 2. python setup.py build 3. python setup.py bdist_wheel 4. pip install dist/*.whl cd. benchmarks/ python benchmark_throughput.py --model /local_model_root/model/qwen-14b-chat/qwen/Qwen-14B-Chat/ --dataset /local_model_root/model/datasets/ShareGPT_V3_unfiltered_cleaned_split.json --trust-remote-code get error blow: Namespace(backend='vllm', dataset='/local_model_root/model/datasets/ShareGPT_V3_unfiltered_cleaned_split.json', input_len=None, output_len=None, model='/local_model_root/model/qwen-14b-chat/qwen/Qwen-14B-Chat/', tokenizer='/local_model_root/model/qwen-14b-chat/qwen/Qwen-14B-Chat/', quantization=None, tensor_parallel_size=1, n=1, use_beam_search=False, num_prompts=1000, seed=0, hf_max_batch_size=None, trust_remote_code=True, max_model_len=None, dtype='auto', gpu_memory_utilization=0.9, enforce_eager=False, kv_cache_dtype='auto', quantization_param_path=None, device='cuda', enable_prefix_caching=False,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: `text The output of `python collect_env.py` ``` ### 🐛 Describe the bug compile steps： 1. pip install -r requirements-build.txt ；pip install -r requirements-dev.txt ；pip install -r requirements-common.txt ；pip install -r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: pip install dist/*.whl cd. benchmarks/ python benchmark_throughput.py --model /local_model_root/model/qwen-14b-chat/qwen/Qwen-14B-Chat/ --dataset /local_model_root/model/datasets/ShareGPT_V3_unfiltered_cleaned_split.jso...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: , tokenizer='/local_model_root/model/qwen-14b-chat/qwen/Qwen-14B-Chat/', quantization=None, tensor_parallel_size=1, n=1, use_beam_search=False, num_prompts=1000, seed=0, hf_max_batch_size=None, trust_remote_code=True, m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]:vllm-0.4.2 running error bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug compile steps： 1. pip install -r requirements-build.txt ；pip install -r requ...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ltered_cleaned_split.json --trust-remote-code get error blow: Namespace(backend='vllm', dataset='/local_model_root/model/datasets/ShareGPT_V3_unfiltered_cleaned_split.json', input_len=None, output_len=None, model='/loca...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
