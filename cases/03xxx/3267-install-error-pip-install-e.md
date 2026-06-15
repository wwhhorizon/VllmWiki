# vllm-project/vllm#3267: install error:pip install -e .

| 字段 | 值 |
| --- | --- |
| Issue | [#3267](https://github.com/vllm-project/vllm/issues/3267) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> install error:pip install -e .

### Issue 正文摘录

Obtaining file:///home/house365ai/xxm/vllm2 Installing build dependencies ... done Checking if build backend supports build_editable ... done Getting requirements to build editable ... error error: subprocess-exited-with-error × Getting requirements to build editable did not run successfully. │ exit code: 1 ╰─> [22 lines of output] /tmp/pip-build-env-wmgabzo_/overlay/lib/python3.10/site-packages/torch/nn/modules/transformer.py:20: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at ../torch/csrc/utils/tensor_numpy.cpp:84.) device: torch.device = torch.device(torch._C._get_default_device()), # torch.device('cpu'), /home/house365ai/anaconda3/envs/vllm2/bin/python: No module named pip Traceback (most recent call last): File "/home/house365ai/anaconda3/envs/vllm2/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in main() File "/home/house365ai/anaconda3/envs/vllm2/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main json_out['return_val'] = hook(**hook_input['kwargs']) File "/home/house365ai/anaconda3/envs/vllm2/lib/python3.10/site-packages/pip/_vendo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: install error:pip install -e . stale Obtaining file:///home/house365ai/xxm/vllm2 Installing build dependencies ... done Checking if build backend supports build_editable ... done Getting requirements to build edita
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: i/xxm/vllm2 Installing build dependencies ... done Checking if build backend supports build_editable ... done Getting requirements to build editable ... error error: subprocess-exited-with-error × Getting requirements t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .py", line 132, in get_requires_for_build_editable return hook(config_settings) File "/tmp/pip-build-env-wmgabzo_/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 448, in get_requires_for_build_edita...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: install error:pip install -e . stale Obtaining file:///home/house365ai/xxm/vllm2 Installing build dependencies ... done Checking if build backend supports build_editable ... done Getting requirements to build editable ....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
