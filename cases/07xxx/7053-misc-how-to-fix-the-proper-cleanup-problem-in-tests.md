# vllm-project/vllm#7053: [Misc]: how to fix the proper cleanup problem in tests

| 字段 | 值 |
| --- | --- |
| Issue | [#7053](https://github.com/vllm-project/vllm/issues/7053) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: how to fix the proper cleanup problem in tests

### Issue 正文摘录

### Anything you want to discuss about vllm. We are having a very difficult time in cleaning up resources properly, especially in distributed inference. This makes our tests suffer recently. To understand this, we have to understand the process model of `pytest`: For this simple test: ```python import pytest @pytest.mark.parametrize('arg', [1, 2, 3]) def test_pass(arg): import os print((arg, os.getpid())) ``` `pytest` will create one process, to run all the three tests one by one. So the output is (Note the process id is the same for three tests): ```text testf.py::test_pass[1] (1, 15068) PASSED testf.py::test_pass[2] (2, 15068) PASSED testf.py::test_pass[3] (3, 15068) PASSED ``` The fact that these three tests share the same process, makes some low-level handling difficult. 1. when some test segfaults, the following test will not run because the process died. For example: ```python import pytest @pytest.mark.parametrize('arg', [1, 2, 3]) def test_pass(arg): import os print((arg, os.getpid())) if arg == 2: import ctypes func_ptr = ctypes.CFUNCTYPE(ctypes.c_int)(0) # Calling the function pointer with an invalid address will cause a segmentation fault func_ptr() ``` this test produc...

## 现有链接修复摘要

#8727 [Misc] Add conftest plugin for applying forking decorator | #29130 [Test] Fix @create_new_process_for_each_test("fork") in interactive shell pipeline

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: are having a very difficult time in cleaning up resources properly, especially in distributed inference. This makes our tests suffer recently. To understand this, we have to understand the process model of `pytest`: For...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: traceback.print_exc() os._exit(1) else: os._exit(0) else: _pid, _exitcode = os.waitpid(pid, 0) assert _exitcode == 0, f"function {f} failed when called with args {args} and kwargs {kwargs}" return wrappe
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: suffer recently. To understand this, we have to understand the process model of `pytest`: For this simple test: ```python import pytest @pytest.mark.parametrize('arg', [1, 2, 3]) def test_pass(arg): import os print((arg...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: be6aac5/.buildkite/test-pipeline.yaml#L85 this is tedious, and does not scale when we want to test multiple combination of arguments. The proposed solution, is to manually fork: ```python import functools def fork_new_p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: g', [1, 2, 3]) def test_pass(arg): import torch assert not torch.cuda.is_initialized() data = torch.ones(10, 10).cuda() print(data) assert data.sum().item() == 100 ``` In this example, every test need a clean process (...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8727](https://github.com/vllm-project/vllm/pull/8727) | closes_keyword | 0.95 | [Misc] Add conftest plugin for applying forking decorator | FIX #7053 --- <details> <!-- inside this <details> section, markdown rendering does not work, so we use raw html here. --> <summary><b> PR Checklist (Click to Expand) </b>< |
| [#29130](https://github.com/vllm-project/vllm/pull/29130) | mentioned | 0.6 | [Test] Fix @create_new_process_for_each_test("fork") in interactive shell pipeline | e parent and relying on SIG_IGN. Related past PRs: #23795 and #7054 (#7053) /cc @njhill @youkaichao |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
