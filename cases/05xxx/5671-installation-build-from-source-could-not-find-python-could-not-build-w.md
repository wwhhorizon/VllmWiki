# vllm-project/vllm#5671: [Installation]: Build from source: Could NOT find Python. Could not build wheels for vllm.

| 字段 | 值 |
| --- | --- |
| Issue | [#5671](https://github.com/vllm-project/vllm/issues/5671) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Build from source: Could NOT find Python. Could not build wheels for vllm.

### Issue 正文摘录

### Your current environment [Building from source](https://docs.vllm.ai/en/stable/getting_started/installation.html) fails: ```text Building wheels for collected packages: vllm Building editable for vllm (pyproject.toml) ... error error: subprocess-exited-with-error × Building editable for vllm (pyproject.toml) did not run successfully. │ exit code: 1 ╰─> [140 lines of output] running editable_wheel creating /tmp/pip-wheel-7hhn6g95/.tmp-o1qz9bu_/vllm.egg-info writing /tmp/pip-wheel-7hhn6g95/.tmp-o1qz9bu_/vllm.egg-info/PKG-INFO writing dependency_links to /tmp/pip-wheel-7hhn6g95/.tmp-o1qz9bu_/vllm.egg-info/dependency_links.txt writing requirements to /tmp/pip-wheel-7hhn6g95/.tmp-o1qz9bu_/vllm.egg-info/requires.txt writing top-level names to /tmp/pip-wheel-7hhn6g95/.tmp-o1qz9bu_/vllm.egg-info/top_level.txt writing manifest file '/tmp/pip-wheel-7hhn6g95/.tmp-o1qz9bu_/vllm.egg-info/SOURCES.txt' reading manifest file '/tmp/pip-wheel-7hhn6g95/.tmp-o1qz9bu_/vllm.egg-info/SOURCES.txt' reading manifest template 'MANIFEST.in' adding license file 'LICENSE' writing manifest file '/tmp/pip-wheel-7hhn6g95/.tmp-o1qz9bu_/vllm.egg-info/SOURCES.txt' creating '/tmp/pip-wheel-7hhn6g95/.tmp-o1qz9bu_/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 11: [Installation]: Build from source: Could NOT find Python. Could not build wheels for vllm. installation ### Your current environment [Building from source](https://docs.vllm.ai/en/stable/getting_started/installation.html
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: tures - done -- Build type: RelWithDebInfo -- Target device: cuda -- Could NOT find Python (missing: Python_INCLUDE_DIRS Interpreter Development.Module Development.SABIModule) CMake Error at cmake/utils.cmake:10 (messag...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: CMakeLists.txt:43 (find_python_from_executable) -- Configuring incomplete, errors occurred! Traceback (most recent call last): File "/tmp/pip-build-env-95v8121y/overlay/lib/python3.11/site-packages/setuptools/command/ed...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: and/editable_wheel.py", line 357, in _create_wheel_file files, mapping = self._run_build_commands(dist_name, unpacked, lib, tmp) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/tmp/pip-build-env-95v8121y/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ffected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp Vulnerability Spectre v1: Mit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
