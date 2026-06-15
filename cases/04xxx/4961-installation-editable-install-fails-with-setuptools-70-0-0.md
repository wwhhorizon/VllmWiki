# vllm-project/vllm#4961: [Installation]: editable install fails with setuptools 70.0.0

| 字段 | 值 |
| --- | --- |
| Issue | [#4961](https://github.com/vllm-project/vllm/issues/4961) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: editable install fails with setuptools 70.0.0

### Issue 正文摘录

### Your current environment ``` Ubuntu 22.04.4 LTS python 3.10.12 torch 2.1.2+cpu vLLM 0.3.3+neuron205 ``` ### How you are installing vllm ```sh pip3 install -e vllm ``` ## Error message ``` Installing build dependencies ... done Checking if build backend supports build_editable ... done Getting requirements to build editable ... error error: subprocess-exited-with-error × Getting requirements to build editable did not run successfully. │ exit code: 1 ╰─> [21 lines of output] /tmp/pip-build-env-9h8zh2_3/overlay/local/lib/python3.10/dist-packages/torch/nn/modules/transformer.py:20: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at ../torch/csrc/utils/tensor_nu mpy.cpp:84.) device: torch.device = torch.device(torch._C._get_default_device()), # torch.device('cpu'), Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in main() File "/usr/local/lib/python3.10/dist-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main json_out['return_val'] = hook(**hook_input['kwargs']) File "/usr/local/lib/python3.10/dist-packages/pip/_v...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: editable install fails with setuptools 70.0.0 installation ### Your current environment ``` Ubuntu 22.04.4 LTS python 3.10.12 torch 2.1.2+cpu vLLM 0.3.3+neuron205 ``` ### How you are installing vllm ```
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: message ``` Installing build dependencies ... done Checking if build backend supports build_editable ... done Getting requirements to build editable ... error error: subprocess-exited-with-error × Getting requirements t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .py", line 132, in get_requires_for_build_editable return hook(config_settings) File "/tmp/pip-build-env-9h8zh2_3/overlay/local/lib/python3.10/dist-packages/setuptools/build_meta.py", line 448, in get_requires_for_build...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
