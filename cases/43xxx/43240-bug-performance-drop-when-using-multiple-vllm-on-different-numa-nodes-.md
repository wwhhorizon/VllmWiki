# vllm-project/vllm#43240: [Bug]: Performance drop when using multiple VLLM on different numa nodes --> bugs in ompmultiprocessing.py

| 字段 | 值 |
| --- | --- |
| Issue | [#43240](https://github.com/vllm-project/vllm/issues/43240) |
| 状态 | open |
| 标签 | bug;cpu |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Performance drop when using multiple VLLM on different numa nodes --> bugs in ompmultiprocessing.py

### Issue 正文摘录

### Your current environment ## Environment - **vLLM version**: v0.21.0 (`public.ecr.aws/q9t5s3a7/vllm-cpu-release-repo:v0.21.0`) - **Platform**: Intel Xeon 2-socket, 60 cores/socket, HT enabled (240 logical CPUs) - **NUMA layout**: Node 0 = CPUs 0-59,120-179; Node 1 = CPUs 60-119,180-239 - **Orchestrator**: Kubernetes with NRI Balloons policy (cpuset allocation) - **OMP library**: Intel OpenMP (libiomp5.so via LD_PRELOAD) Bug is not related only to setting those variables: `VLLM_CPU_OMP_THREADS_BIND` --> when set to auto `VLLM_CPU_NUM_OF_RESERVED_CPU` ### 🐛 Describe the bug Noticed that when running VLLM on entire system performance is fine , but when running 2 VLLM instances inside pinned to specific cores the performance of each instances differs significantly. Isolated the VLLMs from entire solution and created dockerfiles running 2 VLLM instances. Just change nginx_conf.txt to nginx.conf (needed to pass file to this bug report ) and run: ```bash # Start both vLLM instances + nginx load balancer ./run_bench.sh start # Run benchmark (48 prompts, 32 concurrent, through LB) ./run_bench.sh bench [docker-compose.broken.yml](https://github.com/user-attachments/files/28071993/docker-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: essing.py bug;cpu ### Your current environment ## Environment - **vLLM version**: v0.21.0 (`public.ecr.aws/q9t5s3a7/vllm-cpu-release-repo:v0.21.0`) - **Platform**: Intel Xeon 2-socket, 60 cores/socket, HT enabled (240 l...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: rt both vLLM instances + nginx load balancer ./run_bench.sh start # Run benchmark (48 prompts, 32 concurrent, through LB) ./run_bench.sh bench [docker-compose.broken.yml](https://github.com/user-attachments/files/280719...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: l Xeon 2-socket, 60 cores/socket, HT enabled (240 logical CPUs) - **NUMA layout**: Node 0 = CPUs 0-59,120-179; Node 1 = CPUs 60-119,180-239 - **Orchestrator**: Kubernetes with NRI Balloons policy (cpuset allocation) - *...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: wer ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
