# vllm-project/vllm#27788: [Bug]: vLLM `sleep` broken on `main` AttributeError: 'PrometheusStatLogger' object has no attribute 'gauge_engine_sleep_state'.

| 字段 | 值 |
| --- | --- |
| Issue | [#27788](https://github.com/vllm-project/vllm/issues/27788) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM `sleep` broken on `main` AttributeError: 'PrometheusStatLogger' object has no attribute 'gauge_engine_sleep_state'.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM sleep seems to be broken on `main` right now. Testing with SkyRL + the commit b5d90f740048d43376390a61ca5b77c287505d0e, I get the following error with `.sleep`: ```bash Traceback (most recent call last): File "/home/ray/default/vllm/skyrl/skyrl-train/skyrl_train/entrypoints/main_base.py", line 305, in main ray.get(skyrl_entrypoint.remote(cfg)) File "/home/ray/.cache/uv/builds-v0/.tmpc3hoav/lib/python3.12/site-packages/ray/_private/auto_init_hook.py", line 22, in auto_init_wrapper return fn(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^ File "/home/ray/.cache/uv/builds-v0/.tmpc3hoav/lib/python3.12/site-packages/ray/_private/client_mode_hook.py", line 104, in wrapper return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/home/ray/.cache/uv/builds-v0/.tmpc3hoav/lib/python3.12/site-packages/ray/_private/worker.py", line 2858, in get values, debugger_breakpoint = worker.get_objects(object_refs, timeout=timeout) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/ray/.cache/uv/builds-v0/.tmpc3hoav/lib/python3.12/site-packages/ray/_private/worker.py", line 958, in get_objects raise value.as_instanceof_cause() ray.exceptions.RayTa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: in ray.get(skyrl_entrypoint.remote(cfg)) File "/home/ray/.cache/uv/builds-v0/.tmpc3hoav/lib/python3.12/site-packages/ray/_private/auto_init_hook.py", line 22, in auto_init_wrapper return fn(*args, **kwargs) ^^^^^^^^^^^^...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: rainer inference_engines = create_ray_wrapped_inference_engines_from_config(self.cfg, self.colocate_pg, tokenizer) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/ray/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: model = "hmellor/tiny-random-LlamaForCausalLM" free, total = torch.cuda.mem_get_info() used_bytes_baseline = total - free # in case other process is running from vllm import AsyncEngineArgs,AsyncLLMEngine engine_args =...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: # 🐛 Describe the bug vLLM sleep seems to be broken on `main` right now. Testing with SkyRL + the commit b5d90f740048d43376390a61ca5b77c287505d0e, I get the following error with `.sleep`: ```bash Traceback (most recent c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
