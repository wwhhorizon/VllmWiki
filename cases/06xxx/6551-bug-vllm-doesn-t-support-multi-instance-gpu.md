# vllm-project/vllm#6551: [Bug]: vllm doesn't support multi-instance GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#6551](https://github.com/vllm-project/vllm/issues/6551) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 33; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm doesn't support multi-instance GPU

### Issue 正文摘录

### Your current environment ``` Collecting environment information... /nix/store/ar0r42s7ygg1h1clhr5i3k50zbqyrf8c-python3-3.11.9-env/lib/python3.11/site-packages/vllm/usage/usage_lib.py:19: RuntimeWarning: Failed to read commit hash: No module named 'vllm.commit_id' from vllm.version import __version__ as VLLM_VERSION Traceback (most recent call last): File "/nix/store/ar0r42s7ygg1h1clhr5i3k50zbqyrf8c-python3-3.11.9-env/lib/python3.11/site-packages/torch/cuda/__init__.py", line 306, in _lazy_init queued_call() File "/nix/store/ar0r42s7ygg1h1clhr5i3k50zbqyrf8c-python3-3.11.9-env/lib/python3.11/site-packages/torch/cuda/__init__.py", line 174, in _check_capability capability = get_device_capability(d) ^^^^^^^^^^^^^^^^^^^^^^^^ File "/nix/store/ar0r42s7ygg1h1clhr5i3k50zbqyrf8c-python3-3.11.9-env/lib/python3.11/site-packages/torch/cuda/__init__.py", line 430, in get_device_capability prop = get_device_properties(device) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/nix/store/ar0r42s7ygg1h1clhr5i3k50zbqyrf8c-python3-3.11.9-env/lib/python3.11/site-packages/torch/cuda/__init__.py", line 448, in get_device_properties return _get_device_properties(device) # type: ignore[name-defined] ^^^^^^^^^^^^^^^...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Failed to read commit hash: No module named 'vllm.commit_id' from vllm.version import __version__ as VLLM_VERSION Traceback (most recent call last): File "/nix/store/ar0r42s7ygg1h1clhr5i3k50zbqyrf8c-python3-3.11.9-env/l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: tance GPU bug ### Your current environment ``` Collecting environment information... /nix/store/ar0r42s7ygg1h1clhr5i3k50zbqyrf8c-python3-3.11.9-env/lib/python3.11/site-packages/vllm/usage/usage_lib.py:19: RuntimeWarning...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: clhr5i3k50zbqyrf8c-python3-3.11.9-env/lib/python3.11/site-packages/torch/cuda/__init__.py", line 306, in _lazy_init queued_call() File "/nix/store/ar0r42s7ygg1h1clhr5i3k50zbqyrf8c-python3-3.11.9-env/lib/python3.11/site-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ib/python3.11/site-packages/vllm/scripts.py", line 148, in main args.dispatch_function(args) File "/nix/store/ar0r42s7ygg1h1clhr5i3k50zbqyrf8c-python3-3.11.9-env/lib/python3.11/site-packages/vllm/scripts.py", line 28, i...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: E_DEVICES=MIG- nixGL vllm serve NousResearch/Meta-Llama-3-8B-Instruct --dtype auto --api-key token-abc123 ``` you get ``` Traceback (most recent call last): File "/nix/store/91r5lqqzw1bv7xvvyn8kc8b3bmlyyimv-python3.11-v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
