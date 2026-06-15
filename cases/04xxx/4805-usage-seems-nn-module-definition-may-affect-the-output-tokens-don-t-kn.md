# vllm-project/vllm#4805: [Usage]: Seems nn.module definition may affect the output tokens. Don't know the reason.

| 字段 | 值 |
| --- | --- |
| Issue | [#4805](https://github.com/vllm-project/vllm/issues/4805) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Seems nn.module definition may affect the output tokens. Don't know the reason.

### Issue 正文摘录

### Your current environment Env: CPU device vllm: 0.4.2+cpu ```python from vllm import LLM import torch prompts = ["你好"] llm1 = LLM(model="/home/zhenzhong/model/chatglm2-6b", trust_remote_code=True) # Create an LLM. torch.nn.Linear(in_features=4096,out_features=4608, bias=True, dtype=torch.bfloat16) outputs1 = llm1.generate(prompts) # Generate texts from the prompts. llm2= LLM(model="/home/zhenzhong/model/chatglm2-6b", trust_remote_code=True) # Create an LLM. torch.nn.Linear(in_features=4096,out_features=4608, bias=True, dtype=torch.bfloat16) outputs2 = llm2.generate(prompts) # Generate texts from the prompts. llm3= LLM(model="/home/zhenzhong/model/chatglm2-6b", trust_remote_code=True) # Create an LLM. outputs3 = llm3.generate(prompts) # Generate texts from the prompts. print("outputs1 = ", outputs1) print("outputs2 = ", outputs2) print("outputs3 = ", outputs3) ``` For this code, as long as I define the torch.nn.modules in the domain of the current vLLM model, it affects ouput token results even I don't use them. In other words, If I move theses nn.modules I don't use to the above of LLM() definition, it does't affect results. llm1 is the same as llm2, because they both define th...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e an LLM. torch.nn.Linear(in_features=4096,out_features=4608, bias=True, dtype=torch.bfloat16) outputs1 = llm1.generate(prompts) # Generate texts from the prompts. llm2= LLM(model="/home/zhenzhong/model/chatglm2-6b", tr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: le definition may affect the output tokens. Don't know the reason. usage;stale ### Your current environment Env: CPU device vllm: 0.4.2+cpu ```python from vllm import LLM import torch prompts = ["你好"] llm1 = LLM(model="...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: urrent environment Env: CPU device vllm: 0.4.2+cpu ```python from vllm import LLM import torch prompts = ["你好"] llm1 = LLM(model="/home/zhenzhong/model/chatglm2-6b", trust_remote_code=True) # Create an LLM. torch.nn.Lin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ```python from vllm import LLM import torch prompts = ["你好"] llm1 = LLM(model="/home/zhenzhong/model/chatglm2-6b", trust_remote_code=True) # Create an LLM. torch.nn.Linear(in_features=4096,out_features=4608, bias=True,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
