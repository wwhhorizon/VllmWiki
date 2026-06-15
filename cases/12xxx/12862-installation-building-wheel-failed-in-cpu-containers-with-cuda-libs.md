# vllm-project/vllm#12862: [Installation]: building wheel failed in CPU containers with CUDA libs

| 字段 | 值 |
| --- | --- |
| Issue | [#12862](https://github.com/vllm-project/vllm/issues/12862) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: building wheel failed in CPU containers with CUDA libs

### Issue 正文摘录

### Your current environment I‘m trying to build a vllm wheel in a CPU container that has CUDA libs installed. However, there is a link error: ```text [5/265] Linking CXX shared module cumem_allocator.abi3.so FAILED: cumem_allocator.abi3.so : && ccache /usr/local/bin/c++ -fPIC -O3 -DNDEBUG -shared -o cumem_allocator.abi3.so CMakeFiles/cumem_allocator.dir/csrc/cumem_allocator.cpp.o -L/lib/intel64 -L/lib/intel64_win -L/lib/win-x64 -Wl,-rpath,/lib/intel64:/lib/intel64_win:/lib/win-x64:/opt/conda/lib/python3.10/site-packages/torch/lib:/usr/local/cuda/lib64: -lcuda /opt/conda/lib/python3.10/site-packages/torch/lib/libtorch.so /opt/conda/lib/python3.10/site-packages/torch/lib/libc10.so /usr/local/cuda/lib64/libnvrtc.so /opt/conda/lib/python3.10/site-packages/torch/lib/libc10_cuda.so -Wl,--no-as-needed,"/opt/conda/lib/python3.10/site-packages/torch/lib/libtorch_cpu.so" -Wl,--as-needed -Wl,--no-as-needed,"/opt/conda/lib/python3.10/site-packages/torch/lib/libtorch_cuda.so" -Wl,--as-needed /opt/conda/lib/python3.10/site-packages/torch/lib/libc10_cuda.so /opt/conda/lib/python3.10/site-packages/torch/lib/libc10.so /usr/local/cuda/lib64/libcudart.so -Wl,--no-as-needed,"/opt/conda/lib/python3.1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 11: [Installation]: building wheel failed in CPU containers with CUDA libs installation ### Your current environment I‘m trying to build a vllm wheel in a CPU container that has CUDA libs installed. However, there is a link
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Installation]: building wheel failed in CPU containers with CUDA libs installation ### Your current environment I‘m trying to build a vllm wheel in a CPU container that has CUDA libs installed. However, there is a link...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: vllm.version import __version__ as VLLM_VERSION Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Alibaba Group...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.5.1 [pip3] torchvision==0.20.1 [pip3] transformers==4.47.1 [pip3] triton==3.1.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.4.5.8 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.4.127
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: es/torch/lib/libtorch.so" -Wl,--as-needed /usr/local/cuda/lib64/libnvToolsExt.so && : /usr/bin/ld: cannot find -lcuda collect2: error: ld returned 1 exit status ``` I won't find the same error in a GPU container. It loo...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
