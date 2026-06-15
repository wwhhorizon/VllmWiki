# vllm-project/vllm#3265: Issues with installing from source due to flash-attn subprocess install

| 字段 | 值 |
| --- | --- |
| Issue | [#3265](https://github.com/vllm-project/vllm/issues/3265) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Issues with installing from source due to flash-attn subprocess install

### Issue 正文摘录

I only see this issue after https://github.com/vllm-project/vllm/pull/3005 landed. I've run into the same behavior on two GPU instances that I've used to build vLLM before just a few days ago. The main warning/error seems to be: ``` /tmp/pip-build-env-uskajsfq/overlay/lib/python3.10/site-packages/torch/nn/modules/transformer.py:20: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at ../torch/csrc/utils/tensor_numpy.cpp:84.) device: torch.device = torch.device(torch._C._get_default_device()), # torch.device('cpu'), /root/nm/bin/python3: No module named pip ``` I'm not sure what to make of it, but it seems to be creating a different sub-environment and trying to use that. I definitely have things like `numpy` and `pip` installed. Here is my full log running `pip install -e .` with a freshly cloned repo and environment: ``` root@engine-574cfd5988-947g9:~/vllm# pip install -e . Obtaining file:///root/vllm Installing build dependencies ... done Checking if build backend supports build_editable ... done Getting requirements to build editable ... error error: subprocess-exited-with-error × Getting requirements to build editable did not run successful...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Issues with installing from source due to flash-attn subprocess install I only see this issue after https://github.com/vllm-project/vllm/pull/3005 landed. I've run into the same behavior on two GPU instances that I've u...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: //root/vllm Installing build dependencies ... done Checking if build backend supports build_editable ... done Getting requirements to build editable ... error error: subprocess-exited-with-error × Getting requirements t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .py", line 144, in get_requires_for_build_editable return hook(config_settings) File "/tmp/pip-build-env-uskajsfq/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 448, in get_requires_for_build_edita...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
