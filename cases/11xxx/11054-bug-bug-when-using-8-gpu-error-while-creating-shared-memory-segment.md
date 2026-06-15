# vllm-project/vllm#11054: [Bug]: bug when using 8*GPU, Error while creating shared memory segment

| 字段 | 值 |
| --- | --- |
| Issue | [#11054](https://github.com/vllm-project/vllm/issues/11054) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;operator |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: bug when using 8*GPU, Error while creating shared memory segment

### Issue 正文摘录

### Your current environment Version: vllm==0.6.3 nccl==2.20.5 ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am using 8*A100 GPU to run Llama-3.1-70b-chat. Vllm works well for 4*GPU, but fail for 8*GPU, with the following error: `[1;36m(VllmWorkerProcess pid=3184)[0;0m INFO 12-10 11:33:24 model_runner_base.py:149] Completed writing input of failed execution to /tmp/err_execute_model_input_20241210-113324.pkl. [1;36m(VllmWorkerProcess pid=3184)[0;0m ERROR 12-10 11:33:24 multiproc_worker_utils.py:229] Exception in worker VllmWorkerProcess while processing method determine_num_available_blocks. [1;36m(VllmWorkerProcess pid=3184)[0;0m ERROR 12-10 11:33:24 multiproc_worker_utils.py:229] Traceback (most recent call last): [1;36m(VllmWorkerProcess pid=3184)[0;0m ERROR 12-10 11:33:24 multiproc_worker_utils.py:229] File "/sources2/github_vllm/vllm/worker/model_runner_base.py", line 116, in _wrapper [1;36m(VllmWorkerProcess pid=3184)[0;0m ERROR 12-10 11:33:24 multiproc_worker_utils.py:229] return func(*args, **kwargs) [1;36m(VllmWorkerProcess pid=3184)[0;0m ERROR 12-10 11:33:24 multiproc_worker_utils.py:229] File "/sources2/github_vllm/vllm/worker/model_runner.py"...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e creating shared memory segment bug;stale ### Your current environment Version: vllm==0.6.3 nccl==2.20.5 ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am using 8*A100 GPU to run Llama-3.1-70b-chat. Vllm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: # Model Input Dumps _No response_ ### 🐛 Describe the bug I am using 8*A100 GPU to run Llama-3.1-70b-chat. Vllm works well for 4*GPU, but fail for 8*GPU, with the following error: `[1;36m(VllmWorkerProcess pid=3184)[0;...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: it the model shown as follows: `llm = LLM( model=path, dtype=torch.float16, tensor_parallel_size=torch.cuda.device_count(), gpu_memory_utilization=0.9, swap_space=8 ) sampling_params = SamplingParams(n=1, temperature=0,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ale ### Your current environment Version: vllm==0.6.3 nccl==2.20.5 ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am using 8*A100 GPU to run Llama-3.1-70b-chat. Vllm works well for 4*GPU, but fail for 8*GP...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: RROR 12-10 11:33:24 multiproc_worker_utils.py:229] self.model_runner.profile_run() [1;36m(VllmWorkerProcess pid=3184)[0;0m ERROR 12-10 11:33:24 multiproc_worker_utils.py:229] File "/usr/local/conda/lib/python3.9/site-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
