# vllm-project/vllm#19950: [Usage]: 使用Vllm如何对Qwen3ForSequenceClassification模型进行文本分类加速？

| 字段 | 值 |
| --- | --- |
| Issue | [#19950](https://github.com/vllm-project/vllm/issues/19950) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: 使用Vllm如何对Qwen3ForSequenceClassification模型进行文本分类加速？

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` from fastapi import FastAPI from transformers import AutoTokenizer from pydantic import BaseModel import torch import asyncio from vllm import LLM import os import uvicorn class cls_request(BaseModel): text: str os.environ["CUDA_VISIBLE_DEVICES"] = '0' label_list = ['家用电器', '机械设备', '建筑材料', '电力设备', '商贸零售', '国防军工', '医药生物', '建筑装饰', '电子', '传媒', '基础化工', '美容护理', '社会服务', '计算机', '环保', '汽车', '食品饮料', '轻工制造', '有色金属', '交通运输', '农林牧渔', '公用事业', '房地产', '石油石化', '银行', '钢铁', '通信', '非银金融', '纺织服饰', '煤炭'] app = FastAPI() merged_model_path = "/home/lwl/wordkspace/LLaMA-Factory/Qwen3Classification/checkpoint/merged_model" cls_model = LLM(model=merged_model_path, trust_remote_code=True, dtype='bfloat16', task="classify",max_model_len=2048) cls_tokenizer = AutoTokenizer.from_pretrained(merged_model_path) # 队列和批量处理参数 request_queue = [] BATCH_SIZE = 10 BATCH_TIMEOUT = 0.01 # 秒 @app.on_event("startup") async def startup_event(): asyncio.create_task(batch_worker()) async def batch_worker(): while True: await asyncio.sleep(BATCH_TIMEOUT) if len(request_queue) == 0: continue batch = [] while len(batch) < BATCH_SIZE and request_queue:...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: _model" cls_model = LLM(model=merged_model_path, trust_remote_code=True, dtype='bfloat16', task="classify",max_model_len=2048) cls_tokenizer = AutoTokenizer.from_pretrained(merged_model_path) # 队列和批量处理参数 request_queue =...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: 使用Vllm如何对Qwen3ForSequenceClassification模型进行文本分类加速？ usage ### Your current environment ```text The output of `python collect_env.py` ``` from fastapi import FastAPI from transformers import AutoTokenizer from py...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: import asyncio from vllm import LLM import os import uvicorn class cls_request(BaseModel): text: str os.environ["CUDA_VISIBLE_DEVICES"] = '0' label_list = ['家用电器', '机械设备', '建筑材料', '电力设备', '商贸零售', '国防军工', '医药生物', '建筑装饰',...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ironment ```text The output of `python collect_env.py` ``` from fastapi import FastAPI from transformers import AutoTokenizer from pydantic import BaseModel import torch import asyncio from vllm import LLM import os imp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: import uvicorn class cls_request(BaseModel): text: str os.environ["CUDA_VISIBLE_DEVICES"] = '0' label_list = ['家用电器', '机械设备', '建筑材料', '电力设备', '商贸零售', '国防军工', '医药生物', '建筑装饰', '电子', '传媒', '基础化工', '美容护理', '社会服务', '计算机', '环...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
