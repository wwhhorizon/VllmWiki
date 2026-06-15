# vllm-project/vllm#18789: pip install -e . failed

| 字段 | 值 |
| --- | --- |
| Issue | [#18789](https://github.com/vllm-project/vllm/issues/18789) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | install |
| Operator 关键词 | attention;cuda;kernel;moe;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> pip install -e . failed

### Issue 正文摘录

### Your current environment No module named 'numpy' × Building editable for vllm (pyproject.toml) did not run successfully. │ exit code: 1 ╰─> [541 lines of output] /tmp/pip-build-env-_pl3h8ke/overlay/lib/python3.10/site-packages/torch/_subclasses/functional_tensor.py:276: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at /pytorch/torch/csrc/utils/tensor_numpy.cpp:81.) cpu = _conversion_method_template(device=torch.device("cpu")) running editable_wheel creating /tmp/pip-wheel-a7zxip6g/.tmp-t3dsx5by/vllm.egg-info writing /tmp/pip-wheel-a7zxip6g/.tmp-t3dsx5by/vllm.egg-info/PKG-INFO writing dependency_links to /tmp/pip-wheel-a7zxip6g/.tmp-t3dsx5by/vllm.egg-info/dependency_links.txt writing entry points to /tmp/pip-wheel-a7zxip6g/.tmp-t3dsx5by/vllm.egg-info/entry_points.txt writing requirements to /tmp/pip-wheel-a7zxip6g/.tmp-t3dsx5by/vllm.egg-info/requires.txt writing top-level names to /tmp/pip-wheel-a7zxip6g/.tmp-t3dsx5by/vllm.egg-info/top_level.txt writing manifest file '/tmp/pip-wheel-a7zxip6g/.tmp-t3dsx5by/vllm.egg-info/SOURCES.txt' reading manifest template 'MANIFEST.in' adding license file 'LICENSE' writing manifest file '/tmp/pip-wheel...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: pip install -e . failed installation;stale ### Your current environment No module named 'numpy' × Building editable for vllm (pyproject.toml) did not run successfully. │ exit code: 1 ╰─> [541 lines of output] /tm
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: -- Building AllSpark kernels for archs: 8.0 -- Not building scaled_mm_c3x_sm90 as no compatible archs found in CUDA target architectures -- Not building scaled_mm_c3x_100 as no compatible archs found in CUDA target arch...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: tures - done -- Build type: RelWithDebInfo -- Target device: cuda -- Found Python: /home/house365ai/anaconda3/envs/vllm6/bin/python3.10 (found version "3.10.16") found components: Interpreter Development.Module Developm...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: abling cumem allocator extension. -- CMake Version: 4.0.2 -- CUTLASS 3.9.2 -- Found CUDAToolkit: /usr/local/cuda-12.2/targets/x86_64-linux/include (found version "12.2.91") -- CUDART: /usr/local/cuda-12.2/lib64/libcudar...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: and/editable_wheel.py", line 340, in _create_wheel_file files, mapping = self._run_build_commands(dist_name, unpacked, lib, tmp) File "/tmp/pip-build-env-_pl3h8ke/overlay/lib/python3.10/site-packages/setuptools/command/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
