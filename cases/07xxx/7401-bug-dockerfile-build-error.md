# vllm-project/vllm#7401: [Bug]:  Dockerfile build error

| 字段 | 值 |
| --- | --- |
| Issue | [#7401](https://github.com/vllm-project/vllm/issues/7401) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;moe |
| 子分类 | install |
| Operator 关键词 | cuda;moe |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Dockerfile build error

### Issue 正文摘录

### Your current environment docker desktop is used to build the image ### How you are installing vllm so i am trying to build vllm using the dockerfile in the source code locally but the build fails with the error LegacyKeyValueFormat: "ENV key=value" should be used instead of legacy "ENV key value" format (line 229) => [build 13/16] RUN --mount=type=cache,target=/root/.cache/pip if [ "$USE_SCCACHE" = "1" ]; then echo "Installing sccache..." && curl -L -o sccache.tar.gz https://git 0.7s => [build 14/16] RUN --mount=type=cache,target=/root/.cache/ccache --mount=type=cache,target=/root/.cache/pip if [ "$USE_SCCACHE" != "1" ]; then python3 setup.py bdist_w 462.4s => => # -- Build files have been written to: /workspace/build/temp.linux-x86_64-cpython-310 => => # Using MAX_JOBS=8 as the number of jobs. => => # Using NVCC_THREADS=2 as the number of nvcc threads. => => # [1/33] Building CXX object CMakeFiles/_core_C.dir/csrc/core/torch_bindings.cpp.o => => # [2/33] Linking CXX shared module /workspace/build/lib.linux-x86_64-cpython-310/vllm/_core_C.abi3.so => => # [3/33] Building CXX object CMakeFiles/_moe_C.dir/csrc/moe/torch_bindings.cpp.o 3 warnings found (use --debug to expand): - F...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: Dockerfile build error installation;stale ### Your current environment docker desktop is used to build the image ### How you are installing vllm so i am trying to build vllm using the dockerfile in the source cod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: c = error reading from server: EOF development ci_build;frontend_api;moe cuda;moe build_error env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: he source code locally but the build fails with the error LegacyKeyValueFormat: "ENV key=value" should be used instead of legacy "ENV key value" format (line 229) => [build 13/16] RUN --mount=type=cache,target=/root/.ca...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: 310/vllm/_core_C.abi3.so => => # [3/33] Building CXX object CMakeFiles/_moe_C.dir/csrc/moe/torch_bindings.cpp.o 3 warnings found (use --debug to expand): - FromAsCasing: 'as' and 'FROM' keywords' casing do not match (li...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Dockerfile build error installation;stale ### Your current environment docker desktop is used to build the image ### How you are installing vllm so i am trying to build vllm using the dockerfile in the source cod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
