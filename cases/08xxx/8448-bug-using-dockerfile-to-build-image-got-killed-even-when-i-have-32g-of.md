# vllm-project/vllm#8448: [Bug]: using Dockerfile to build image got Killed,even when I have 32g of ram

| 字段 | 值 |
| --- | --- |
| Issue | [#8448](https://github.com/vllm-project/vllm/issues/8448) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: using Dockerfile to build image got Killed,even when I have 32g of ram

### Issue 正文摘录

[+] Building 1731.5s (28/34) => CACHED [base 4/7] WORKDIR /workspace 0.0s => CACHED [base 5/7] COPY requirements-common.txt requirements-common.txt 0.0s => CACHED [base 6/7] COPY requirements-cuda.txt requirements-cuda.txt 0.0s => CACHED [base 7/7] RUN --mount=type=cache,target=/root/.cache/pip python3 -m pip install -r r 0.0s => CACHED [build 1/14] COPY requirements-build.txt requirements-build.txt 0.0s => CACHED [build 2/14] RUN --mount=type=cache,target=/root/.cache/pip python3 -m pip install - 0.0s => CACHED [build 3/14] COPY csrc csrc 0.0s => CACHED [build 4/14] COPY setup.py setup.py 0.0s => CACHED [build 5/14] COPY cmake cmake 0.0s => CACHED [build 6/14] COPY CMakeLists.txt CMakeLists.txt 0.0s => CACHED [build 7/14] COPY requirements-common.txt requirements-common.txt 0.0s => CACHED [build 8/14] COPY requirements-cuda.txt requirements-cuda.txt 0.0s => CACHED [build 9/14] COPY pyproject.toml pyproject.toml 0.0s => CACHED [build 10/14] COPY vllm vllm 0.0s => CACHED [build 11/14] RUN --mount=type=cache,target=/root/.cache/pip if [ "$USE_SCCACHE" = "1 0.0s => [build 12/14] RUN --mount=type=cache,target=/root/.cache/ccache --mount=type=cache,target 1731.3s => => # code=[sm_86]"...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: using Dockerfile to build image got Killed,even when I have 32g of ram bug;stale [+] Building 1731.5s (28/34) => CACHED [base 4/7] WORKDIR /worksp
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 0.0s => CACHED [base 6/7] COPY requirements-cuda.txt requirements-cuda.txt 0.0s => CACHED [base 7/7] RUN --mount=type=cache,target=/root/.cache/pip python3 -m pip install -r r 0.0s => CACHED [build 1/14] COPY requiremen...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ompute_90]" -Xcompiler=-fPIC --expt-relaxed-co => => # nstexpr -DENABLE_FP8 --threads=2 -D_GLIBCXX_USE_CXX11_ABI=0 -MD -MT CMakeFiles/_C.dir/csrc/cache_ => => # kernels.cu.o -MF CMakeFiles/_C.dir/csrc/cache_kernels.cu.o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ing Dockerfile to build image got Killed,even when I have 32g of ram bug;stale [+] Building 1731.5s (28/34) => CACHED [base 4/7] WORKDIR /workspace 0.0s

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
