# vllm-project/vllm#2793: 0.2.7 CPU Memory Leak - MPT-7B tensor_parallel_size=4

| 字段 | 值 |
| --- | --- |
| Issue | [#2793](https://github.com/vllm-project/vllm/issues/2793) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | hardware_porting |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> 0.2.7 CPU Memory Leak - MPT-7B tensor_parallel_size=4

### Issue 正文摘录

I am running `mosaicml/mpt-7b` on `vllm==0.2.7`, with `cuda==12.1` on a `g5.12xlarge` instance and after continuous use I get an Out of Memory error from my CPU's memory. Below is my script for minimum reproducibility. ``` from vllm import LLM import psutil llm = LLM("mosaicml/mpt-7b", trust_remote_code=True, tensor_parallel_size=4) for i in range(0, 100000): output = llm.generate("San Franciso is a") if i % 1000 == 0: cpu_percent = psutil.cpu_percent() memory_percent = psutil.virtual_memory().percent with open("cpu_memory.log","a") as f: f.write(f"Iteration number: {i}\n") f.write(f"CPU utilization: {cpu_percent}%\n") f.write(f"Memory utilization: {memory_percent}%\n") f.write("=========================================\n") print("Done!") ``` Running the above script for a while shows a starting CPU Memory usage % of 14.5% and by 20,000 inferences 21%. Previously, `vllm==0.2.1`, we were able to run our endpoint continuously without an OOM causing a restart but now it will OOM every 8 hours or so.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Memory error from my CPU's memory. Below is my script for minimum reproducibility. ``` from vllm import LLM import psutil llm = LLM("mosaicml/mpt-7b", trust_remote_code=True, tensor_parallel_size=4) for i in range(0, 10...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: r_parallel_size=4 I am running `mosaicml/mpt-7b` on `vllm==0.2.7`, with `cuda==12.1` on a `g5.12xlarge` instance and after continuous use I get an Out of Memory error from my CPU's memory. Below is my script for minimum...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: `vllm==0.2.1`, we were able to run our endpoint continuously without an OOM causing a restart but now it will OOM every 8 hours or so. performance hardware_porting cuda oom I am running `mosaicml/mpt-7b` on `vllm==0.2.7...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
