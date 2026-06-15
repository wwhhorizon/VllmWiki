# vllm-project/vllm#15790: [Bug]: xgrammar==0.17 not work when guided

| 字段 | 值 |
| --- | --- |
| Issue | [#15790](https://github.com/vllm-project/vllm/issues/15790) |
| 状态 | closed |
| 标签 | bug;structured-output;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: xgrammar==0.17 not work when guided

### Issue 正文摘录

### Your current environment from pydantic import BaseModel from openai import OpenAI import json import tiktoken from pydantic import BaseModel, Field from typing import Annotated def count_tokens(text, model="gpt-3.5-turbo"): """计算文本的token数量""" encoder = tiktoken.encoding_for_model(model) tokens = encoder.encode(text) return len(tokens) # 使用示例 text = "你好，这是一个示例文本。" token_count = count_tokens(text) print(f"Token数量: {token_count}") class Info(BaseModel): name: Annotated[str, Field(max_length=10)] age: int json_schema = Info.model_json_schema() print(json_schema) print(count_tokens(json.dumps(json_schema))) client = OpenAI( api_key="sk-aa27cd8dfad346a6b576e51e68aa7283", base_url="http://127.0.0.1:5000/v1", ) char_ls = ["东", "男", "西", "被"] import numpy as np for i in range(10): ii = np.random.randint(len(char_ls)) char_zifu = char_ls[ii] print(char_zifu * 10) ques = char_zifu * 10000 completion = client.chat.completions.create( model="Qwen2.5-VL-3B-Instruct", messages=[ { "role": "system", "content": "You must respond with JSON containing name and age fields.", }, {"role": "user", "content": ques[:2000]}, ], extra_body={ "guided_json": json_schema, "guided_decoding_backend": "xgramm...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ured-output;stale ### Your current environment from pydantic import BaseModel from openai import OpenAI import json import tiktoken from pydantic import BaseModel, Field from typing import Annotated def count_tokens(tex...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: y={ "guided_json": json_schema, "guided_decoding_backend": "xgrammar", # 尝试不同的后端lm-format-enforcer # "use_cache": False, }, # temperature=0.01, # top_p=0.9, ) content = completion.choices[0].message.content print(content
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: bug;structured-output;stale ### Your current environment from pydantic import BaseModel from openai import OpenAI import json import tiktoken from pydantic import BaseModel, Field from typing import Annotated def count_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 男男男 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ": "xgrammar", # 尝试不同的后端lm-format-enforcer # "use_cache": False, }, # temperature=0.01, # top_p=0.9, ) content = completion.choices[0].message.content print(content) # 手动解析JSON响应 import json response_json = json.loads(c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
