# vllm-project/vllm#43035: [Build]: spinloop.cpp fails with Py_LIMITED_API enabled: Py_buffer not declared

| 字段 | 值 |
| --- | --- |
| Issue | [#43035](https://github.com/vllm-project/vllm/issues/43035) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Build]: spinloop.cpp fails with Py_LIMITED_API enabled: Py_buffer not declared

### Issue 正文摘录

### Your current environment ;atest ### 🐛 Describe the bug ``` FAILED: [code=1] CMakeFiles/spinloop.dir/csrc/spinloop.cpp.o ccache /usr/bin/g++-12 -DPy_LIMITED_API=0x030b0000 -DTORCH_EXTENSION_NAME=spinloop -DUSE_C10D_GLOO -DUSE_C10D_NCCL -DUSE_DISTRIBUTED -DUSE_NVSHMEM -DUSE_RPC -DUSE_TENSORPIPE -Dspinloop_EXPORTS -I//vllm/cs rc -isystem /root/Miniconda3_sz/envs/qwen3_1/include/python3.10 -isystem /root/Miniconda3_sz/envs/qwen3_1/lib/python3.10/site-packages/torch/include -isystem /root/Miniconda3_sz/envs/qwen3_1/lib/python3.10/site-packages/torch/include/tor ch/csrc/api/include -isystem /usr/local/cuda/include -I/usr/local/cuda/include -O2 -g -DNDEBUG -std=gnu++20 -fPIC -mmwaitx -MD -MT CMakeFiles/spinloop.dir/csrc/spinloop.cpp.o -MF CMakeFiles/spinloop.dir/csrc/spinloop.cpp.o.d -o CMakeFile s/spinloop.dir/csrc/spinloop.cpp.o -c //vllm/csrc/spinloop.cpp /lm/csrc/spinloop.cpp: In function �yObject* method_spinloop(PyObject*, PyObject*, PyObject*)� hork/tools/vllm/csrc/spinloop.cpp:58:3: error: �y_buffer�was not declared in this scope; did you mean �etbuffer� 58 | Py_buffer buffer; | ^~~~~~~~~ | setbuffer ork/tools/vllm/csrc/spinloop.cpp:70:37: error: �uffer�was not declared in th...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Build]: spinloop.cpp fails with Py_LIMITED_API enabled: Py_buffer not declared bug ### Your current environment ;atest ### 🐛 Describe the bug ``` FAILED: [code=1] CMakeFiles/spinloop.dir/csrc/spinloop.cpp.o ccac
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: /site-packages/torch/include/tor ch/csrc/api/include -isystem /usr/local/cuda/include -I/usr/local/cuda/include -O2 -g -DNDEBUG -std=gnu++20 -fPIC -mmwaitx -MD -MT CMakeFiles/spinloop.dir/csrc/spinloop.cpp.o -MF CMakeFi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: PIPE -Dspinloop_EXPORTS -I//vllm/cs rc -isystem /root/Miniconda3_sz/envs/qwen3_1/include/python3.10 -isystem /root/Miniconda3_sz/envs/qwen3_1/lib/python3.10/site-packages/torch/include -isystem /root/Miniconda3_sz/envs/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: I enabled: Py_buffer not declared bug ### Your current environment ;atest ### 🐛 Describe the bug ``` FAILED: [code=1] CMakeFiles/spinloop.dir/csrc/spinloop.cpp.o ccache /usr/bin/g++-12 -DPy_LIMITED_API=0x030b0000 -DTORC...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
