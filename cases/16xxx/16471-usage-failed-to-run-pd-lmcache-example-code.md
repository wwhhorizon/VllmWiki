# vllm-project/vllm#16471: [Usage]: failed to run PD LMCache example code

| 字段 | 值 |
| --- | --- |
| Issue | [#16471](https://github.com/vllm-project/vllm/issues/16471) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: failed to run PD LMCache example code

### Issue 正文摘录

### Your current environment ```text (vllml) root@salab-hpedl380g11-03:~/wayne/kvcache/vllm/examples/offline_inference# python3 collect_env.py Traceback (most recent call last): File "/root/wayne/kvcache/vllm/vllml/lib/python3.12/site-packages/transformers/utils/import_utils.py", line 1967, in _get_module return importlib.import_module("." + module_name, self.__name__) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/lib/python3.12/importlib/__init__.py", line 90, in import_module return _bootstrap._gcd_import(name[level:], package, level) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File " ", line 1387, in _gcd_import File " ", line 1360, in _find_and_load File " ", line 1331, in _find_and_load_unlocked File " ", line 935, in _load_unlocked File " ", line 995, in exec_module File " ", line 488, in _call_with_frames_removed File "/root/wayne/kvcache/vllm/vllml/lib/python3.12/site-packages/transformers/processing_utils.py", line 33, in from .image_utils import ( File "/root/wayne/kvcache/vllm/vllml/lib/python3.12/site-packages/transformers/image_utils.py", line 64, in from torchvision import io as torchvision_io File "/root/wayne/kvcache/vllm/vllml/lib/p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: wayne/kvcache/vllm/vllml/lib/python3.12/site-packages/transformers/utils/import_utils.py", line 1967, in _get_module return importlib.import_module("." + module_name, self.__name__) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 10, in from torchvision import _meta_registrations, datasets, io, models, ops, transforms, utils # usort:skip ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/root/wayne/k...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: failed to run PD LMCache example code usage;stale ### Your current environment ```text (vllml) root@salab-hpedl380g11-03:~/wayne/kvcache/vllm/examples/offline_inference# python3 collect_env.py Traceback (most r...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ages/torch/_library/fake_impl.py", line 31, in register if torch._C._dispatch_has_kernel_for_dispatch_key(self.qualname, "Meta"): ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ RuntimeError: opera...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
