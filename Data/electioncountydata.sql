DROP TABLE IF EXISTS electiondata;
CREATE TABLE electiondata (
  state text,
  area text,
  totalvotes int,
  repvotes int,
  repcandidate text,
  demvotes int,
  demcandidates text,
  thirdparty text,
  thirdvotes int,
  thirdcandidate text,
  othervotes int,
  repvotespercent decimal(5,2),
  demvotespercent decimal(5,2),
  thirdvotespercent decimal(5,2),
  othervotespercent decimal(5,2),
  repvotesmajorpercent decimal(5,2),
  demvotesmajorpercent decimal(5,2)
);