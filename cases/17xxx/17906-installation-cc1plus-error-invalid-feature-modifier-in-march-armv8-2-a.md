# vllm-project/vllm#17906: [Installation]: cc1plus: error: invalid feature modifier in ‘-march=armv8.2-a+dotprod+fp16’

| 字段 | 值 |
| --- | --- |
| Issue | [#17906](https://github.com/vllm-project/vllm/issues/17906) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: cc1plus: error: invalid feature modifier in ‘-march=armv8.2-a+dotprod+fp16’

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` -- CPU extension compile flags: -fopenmp;-DVLLM_CPU_EXTENSION;-march=armv8.2-a+dotprod+fp16 -- Enabling C extension. -- Configuring done (3.5s) -- Generating done (0.0s) -- Build files have been written to: /tmp/pip-install-b261gxij/vllm_e99d65c51e5c4cea948384f47668e6c3/build/temp.linux-aarch64-cpython-310 [1/9] Building CXX object CMakeFiles/_C.dir/csrc/cpu/activation.cpp.o FAILED: CMakeFiles/_C.dir/csrc/cpu/activation.cpp.o /usr/bin/c++ -DPy_LIMITED_API=3 -DTORCH_EXTENSION_NAME=_C -DUSE_C10D_GLOO -DUSE_DISTRIBUTED -DUSE_RPC -DUSE_TENSORPIPE -D_C_EXPORTS -I/tmp/pip-install-b261gxij/vllm_e99d65c51e5c4cea948384f47668e6c3/csrc -isystem /home/ma-user/anaconda3/envs/py310/include/python3.10 -isystem /tmp/pip-build-env-mwllr031/overlay/lib/python3.10/site-packages/torch/include -isystem /tmp/pip-build-env-mwllr031/overlay/lib/python3.10/site-packages/torch/include/torch/csrc/api/include -O2 -g -DNDEBUG -std=gnu++1z -fPIC -fopenmp -DVLLM_CPU_EXTENSION -march=armv8.2-a+dotprod+fp16 -D_GLIBCXX_USE_CXX11_ABI=1 -MD -MT CMakeFiles/_C.dir/csrc/cpu/activation.cpp.o -MF CMakeFiles/_C.dir/csrc/cpu/activation.cpp.o.d -...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: cc1plus: error: invalid feature modifier in ‘-march=armv8.2-a+dotprod+fp16’ installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` -- CPU extension compile fl
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: invalid feature modifier in ‘-march=armv8.2-a+dotprod+fp16’ installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` -- CPU extension compile flags: -fopenmp;-DVLLM_CPU_EXTENSION...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Installation]: cc1plus: error: invalid feature modifier in ‘-march=armv8.2-a+dotprod+fp16’ installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` -- CPU extension compile flag...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ON;-march=armv8.2-a+dotprod+fp16 -- Enabling C extension. -- Configuring done (3.5s) -- Generating done (0.0s) -- Build files have been written to: /tmp/pip-install-b261gxij/vllm_e99d65c51e5c4cea948384f47668e6c3/build/t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
