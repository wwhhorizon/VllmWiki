# vllm-project/vllm#2720: instal from sourece error:  compiler_compat/ld: cannot find -lcuda

| 字段 | 值 |
| --- | --- |
| Issue | [#2720](https://github.com/vllm-project/vllm/issues/2720) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;attention_kv_cache;ci_build;frontend_api;gemm_linear;model_support;moe;quantization;scheduler_memory |
| 子分类 | install |
| Operator 关键词 | activation;attention;cuda;quantization |
| 症状 | build_error |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> instal from sourece error:  compiler_compat/ld: cannot find -lcuda

### Issue 正文摘录

**Here are the errors. l failed to install the vllm0.3.0 from source. CUDA==12.1** the install log is shown belown `(py310_cu121_vllm) [ vllm-0.3.0]$ proxychains4 python setup.py install running install /data01/rhino_xsg/software/anaconda3/envs/py310_cu121_vllm/lib/python3.10/site-packages/setuptools/_distutils/cmd.py:66: running bdist_egg running egg_info creating vllm.egg-info writing vllm.egg-info/PKG-INFO writing dependency_links to vllm.egg-info/dependency_links.txt writing requirements to vllm.egg-info/requires.txt writing top-level names to vllm.egg-info/top_level.txt writing manifest file 'vllm.egg-info/SOURCES.txt' reading manifest file 'vllm.egg-info/SOURCES.txt' reading manifest template 'MANIFEST.in' adding license file 'LICENSE' writing manifest file 'vllm.egg-info/SOURCES.txt' installing library code to build/bdist.linux-x86_64/egg running install_lib running build_py creating build creating build/lib.linux-x86_64-cpython-310 creating build/lib.linux-x86_64-cpython-310/vllm copying vllm/block.py -> build/lib.linux-x86_64-cpython-310/vllm copying vllm/outputs.py -> build/lib.linux-x86_64-cpython-310/vllm copying vllm/sampling_params.py -> build/lib.linux-x86_64-cpytho...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: instal from sourece error: compiler_compat/ld: cannot find -lcuda **Here are the errors. l failed to install the vllm0.3.0 from source. CUDA==12.1** the install log is shown belown `(py310_cu121_vllm) [ vllm-0.3.0]$ pro...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 10/vllm/model_executor/models copying vllm/model_executor/models/mixtral_quant.py -> build/lib.linux-x86_64-cpython-310/vllm/model_executor/models copying vllm/model_executor/models/baichuan.py -> build/lib.linux-x86_64...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: mpling_params.py -> build/lib.linux-x86_64-cpython-310/vllm copying vllm/config.py -> build/lib.linux-x86_64-cpython-310/vllm copying vllm/test_utils.py -> build/lib.linux-x86_64-cpython-310/vllm copying vllm/utils.py -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: creating build/lib.linux-x86_64-cpython-310/vllm/core copying vllm/core/scheduler.py -> build/lib.linux-x86_64-cpython-310/vllm/core copying vllm/core/__init__.py -> build/lib.linux-x86_64-cpython-310/vllm/core copying...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: instal from sourece error: compiler_compat/ld: cannot find -lcuda **Here are the errors. l failed to install the vllm0.3.0 from source. CUDA==12.1** the install log is shown belown `(py310_cu121_vllm) [ vllm-0.3.0]$ pro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
