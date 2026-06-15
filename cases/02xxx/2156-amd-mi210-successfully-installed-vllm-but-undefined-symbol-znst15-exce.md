# vllm-project/vllm#2156: AMD MI210 successfully installed vllm but undefined symbol _ZNSt15__exception_ptr13exception_ptr9_M_addrefEv

| 字段 | 值 |
| --- | --- |
| Issue | [#2156](https://github.com/vllm-project/vllm/issues/2156) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AMD MI210 successfully installed vllm but undefined symbol _ZNSt15__exception_ptr13exception_ptr9_M_addrefEv

### Issue 正文摘录

`(vllm_rocm) [yys@v100 examples]$ python offline_inference.py /home/yys/anaconda_install/envs/vllm_rocm/lib/python3.8/site-packages/transformers/utils/generic.py:441: UserWarning: torch.utils._pytree._register_pytree_node is deprecated. Please use torch.utils._pytree.register_pytree_node instead. _torch_pytree._register_pytree_node( Traceback (most recent call last): File "offline_inference.py", line 1, in from vllm import LLM, SamplingParams File "/home/yys/anaconda_install/envs/vllm_rocm/lib/python3.8/site-packages/vllm-0.2.4+rocm573-py3.8-linux-x86_64.egg/vllm/__init__.py", line 3, in from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs File "/home/yys/anaconda_install/envs/vllm_rocm/lib/python3.8/site-packages/vllm-0.2.4+rocm573-py3.8-linux-x86_64.egg/vllm/engine/arg_utils.py", line 6, in from vllm.config import (CacheConfig, ModelConfig, ParallelConfig, File "/home/yys/anaconda_install/envs/vllm_rocm/lib/python3.8/site-packages/vllm-0.2.4+rocm573-py3.8-linux-x86_64.egg/vllm/config.py", line 9, in from vllm.utils import get_cpu_memory, is_hip File "/home/yys/anaconda_install/envs/vllm_rocm/lib/python3.8/site-packages/vllm-0.2.4+rocm573-py3.8-linux-x86_64.egg/vllm/util...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: AMD MI210 successfully installed vllm but undefined symbol _ZNSt15__exception_ptr13exception_ptr9_M_addrefEv `(vllm_rocm) [yys@v100 examples]$ python offline_inference.py /home/yys/anaconda_install/envs/vllm_rocm/lib/py...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ndefined symbol _ZNSt15__exception_ptr13exception_ptr9_M_addrefEv `(vllm_rocm) [yys@v100 examples]$ python offline_inference.py /home/yys/anaconda_install/envs/vllm_rocm/lib/python3.8/site-packages/transformers/utils/ge...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 8-linux-x86_64.egg/vllm/engine/arg_utils.py", line 6, in from vllm.config import (CacheConfig, ModelConfig, ParallelConfig, File "/home/yys/anaconda_install/envs/vllm_rocm/lib/python3.8/site-packages/vllm-0.2.4+rocm573-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
