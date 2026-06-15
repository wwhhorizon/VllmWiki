# vllm-project/vllm#17353: [Installation]:  build link error , how to fix it

| 字段 | 值 |
| --- | --- |
| Issue | [#17353](https://github.com/vllm-project/vllm/issues/17353) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;gemm_linear |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;gemm |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]:  build link error , how to fix it

### Issue 正文摘录

### Your current environment ``` /opt/compiler/gcc-12/bin/g++ -fno-strict-overflow -Wsign-compare -DNDEBUG -O2 -Wall -fPIC -O2 -isystem /mnt/NLP_disk41/zhanghui41/llama3/vllm-env/include -fPIC -O2 -isystem /mnt/NLP_disk41/zhanghui41/llama3/vllm-env/include -pthread -B /mnt/NLP_disk41/zhanghui41/llama3/vllm-env/compiler_compat -shared -Wl,-rpath,/mnt/NLP_disk41/zhanghui41/llama3/vllm-env/lib -Wl,-rpath-link,/mnt/NLP_disk41/zhanghui41/llama3/vllm-env/lib -L/mnt/NLP_disk41/zhanghui41/llama3/vllm-env/lib -Wl,-rpath,/mnt/NLP_disk41/zhanghui41/llama3/vllm-env/lib -Wl,-rpath-link,/mnt/NLP_disk41/zhanghui41/llama3/vllm-env/lib -L/mnt/NLP_disk41/zhanghui41/llama3/vllm-env/lib build/temp.linux-x86_64-cpython-312/xformers/csrc/attention/attention.o build/temp.linux-x86_64-cpython-312/xformers/csrc/attention/autograd/matmul.o build/temp.linux-x86_64-cpython-312/xformers/csrc/attention/cpu/matmul.o build/temp.linux-x86_64-cpython-312/xformers/csrc/attention/cpu/sddmm.o build/temp.linux-x86_64-cpython-312/xformers/csrc/attention/cpu/sparse_softmax.o build/temp.linux-x86_64-cpython-312/xformers/csrc/attention/cpu/spmm.o build/temp.linux-x86_64-cpython-312/xformers/csrc/attention/cuda/matmul.o bu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: build link error , how to fix it installation;stale ### Your current environment ``` /opt/compiler/gcc-12/bin/g++ -fno-strict-overflow -Wsign-compare -DNDEBUG -O2 -Wall -fPIC -O2 -isystem /mnt/NLP_
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n/cpu/spmm.o build/temp.linux-x86_64-cpython-312/xformers/csrc/attention/cuda/matmul.o build/temp.linux-x86_64-cpython-312/xformers/csrc/attention/cuda/sddmm.o build/temp.linux-x86_64-cpython-312/xformers/csrc/attention...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: compare -DNDEBUG -O2 -Wall -fPIC -O2 -isystem /mnt/NLP_disk41/zhanghui41/llama3/vllm-env/include -fPIC -O2 -isystem /mnt/NLP_disk41/zhanghui41/llama3/vllm-env/include -pthread -B /mnt/NLP_disk41/zhanghui41/llama3/vllm-e...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ion_kernels.o build/temp.linux-x86_64-cpython-312/xformers/csrc/sparse24/gemm.o build/temp.linux-x86_64-cpython-312/xformers/csrc/sparse24/meta_utils.o build/temp.linux-x86_64-cpython-312/xformers/csrc/sparse24/sparse24...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: build link error , how to fix it installation;stale ### Your current environment ``` /opt/compiler/gcc-12/bin/g++ -fno-strict-overflow -Wsign-compare -DNDEBUG -O2 -Wall -fPIC -O2 -isystem /mnt/NLP_disk41...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
