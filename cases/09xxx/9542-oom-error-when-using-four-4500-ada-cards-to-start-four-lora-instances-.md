# vllm-project/vllm#9542: OOM error :When using four 4500 ada cards to start four lora instances, an error occurs. However, no error occurs when not starting lora on the four 4500 ada cards, and there is no error when starting four lora instances on a single A100 card.

| 字段 | 值 |
| --- | --- |
| Issue | [#9542](https://github.com/vllm-project/vllm/issues/9542) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | gemm_linear;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | crash;oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> OOM error :When using four 4500 ada cards to start four lora instances, an error occurs. However, no error occurs when not starting lora on the four 4500 ada cards, and there is no error when starting four lora instances on a single A100 card.

### Issue 正文摘录

### Your current environment vllm版本:0.6.2 4500 ada: 24G*4显存 A100: 80G显存 model: yi1.5-34b-chat-16k ### Model Input Dumps [err_execute_model_input_20241021-023236.zip](https://github.com/user-attachments/files/17455192/err_execute_model_input_20241021-023236.zip) ### 🐛 Describe the bug INFO 10-21 02:32:36 model_runner_base.py:120] Writing input of failed execution to /tmp/err_execute_model_input_20241021-023236.pkl... [1;36m(VllmWorkerProcess pid=232)[0;0m INFO 10-21 02:32:36 model_runner_base.py:120] Writing input of failed execution to /tmp/err_execute_model_input_20241021-023236.pkl... [1;36m(VllmWorkerProcess pid=230)[0;0m INFO 10-21 02:32:36 model_runner_base.py:120] Writing input of failed execution to /tmp/err_execute_model_input_20241021-023236.pkl... [1;36m(VllmWorkerProcess pid=231)[0;0m INFO 10-21 02:32:36 model_runner_base.py:120] Writing input of failed execution to /tmp/err_execute_model_input_20241021-023236.pkl... [1;36m(VllmWorkerProcess pid=230)[0;0m INFO 10-21 02:32:36 model_runner_base.py:149] Completed writing input of failed execution to /tmp/err_execute_model_input_20241021-023236.pkl. [1;36m(VllmWorkerProcess pid=232)[0;0m INFO 10-21 02:32:36 model_...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: rds, and there is no error when starting four lora instances on a single A100 card. bug;stale ### Your current environment vllm版本:0.6.2 4500 ada: 24G*4显存 A100: 80G显存 model: yi1.5-34b-chat-16k ### Model Input Dumps [err_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: CUDA out of memory. Tried to allocate 220.00 MiB. GPU 3 has a total capacity of 23.65 GiB of which 100.62 MiB is free. Process 132987 has 23.53 GiB memory in use. Of the allocated memory 21.80 GiB is allocated by PyTorc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### Your current environment vllm版本:0.6.2 4500 ada: 24G*4显存 A100: 80G显存 model: yi1.5-34b-chat-16k ### Model Input Dumps [err_execute_model_input_20241021-023236.zip](https://github.com/user-attachments/files/17455192/er...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: is no error when starting four lora instances on a single A100 card. bug;stale ### Your current environment vllm版本:0.6.2 4500 ada: 24G*4显存 A100: 80G显存 model: yi1.5-34b-chat-16k ### Model Input Dumps [err_execute_model_i...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: -21 02:32:36 multiproc_worker_utils.py:233] output = self.base_layer.quant_method.apply(self.base_layer, x) [1;36m(VllmWorkerProcess pid=232)[0;0m ERROR 10-21 02:32:36 multiproc_worker_utils.py:233] File "/usr/local/l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
